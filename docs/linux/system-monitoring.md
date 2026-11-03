# Linux Performance Monitoring and Troubleshooting

Use this guide as a practical reference for diagnosing CPU, memory,
process, and storage-I/O problems on Linux hosts. It focuses on five
commands:

-   `top` --- live system and process view
-   `ps` --- point-in-time process inspection
-   `free` --- memory and swap summary
-   `vmstat` --- system-wide CPU, memory, scheduler, and I/O activity
-   `iostat` --- CPU and block-device I/O statistics

The goal is not to memorize output columns. It is to build a repeatable
investigation: establish impact, take a short baseline, identify the
constrained resource, correlate independent signals, and choose a safe
next action.

------------------------------------------------------------------------

## 1. A safe troubleshooting workflow

When a production host is slow or an application is unhealthy:

1.  **Establish impact.** Identify affected service, nodes, users,
    regions, and the start time. Check whether the issue is host-wide or
    isolated to one process, container, or cgroup.
2.  **Capture a short baseline.** Use read-oriented commands first.
    Avoid starting profilers, tracing every syscall, dumping huge files,
    or repeatedly running expensive commands on an already stressed
    host.
3.  **Check the time dimension.** A single snapshot is not a trend.
    Repeat measurements at a known interval and compare them with
    application latency, throughput, errors, and deployment events.
4.  **Correlate signals.** For example, high CPU in `top` plus a growing
    run queue in `vmstat` is stronger evidence of CPU pressure than
    either metric alone.
5.  **Check the execution boundary.** Host-level CPU and memory can hide
    container limits, CPU throttling, memory limits, and per-cgroup
    pressure.
6.  **Mitigate safely.** Prefer reversible actions such as stopping a
    rollout, reducing concurrency, shifting traffic, or scaling
    capacity. Preserve evidence and follow incident/change procedures.

### Quick command sequence

``` bash
# Overall live view
top

# Processes ranked by CPU
ps -eo pid,ppid,stat,%cpu,%mem,rss,etime,cmd --sort=-%cpu | head -20

# Memory in human-readable units
free -h

# System activity at one-second intervals
vmstat 1 6

# Extended CPU and device statistics
iostat -xz 1 6
```

The first `vmstat` and `iostat` reports commonly represent averages
since boot. For interval troubleshooting, interpret the later reports as
the meaningful samples. Some sysstat versions support `iostat -y` to
suppress the initial report.

------------------------------------------------------------------------

## 2. `top` --- live system and process monitoring

### What it answers

`top` provides a continuously refreshed view of system load, CPU states,
memory, swap, and processes or threads. It is useful when you need to
see whether a symptom is happening now and which processes appear to be
responsible.

``` bash
top
```

Useful alternatives:

``` bash
top -b -n 3                 # Batch output; three snapshots
top -b -d 2 -n 5             # Five snapshots, two seconds apart
top -H -p <PID>              # Show threads belonging to a process
top -p <PID>                 # Focus on one process
```

### Understand the header

  -----------------------------------------------------------------------
  Field                   Meaning                 How to interpret it
  ----------------------- ----------------------- -----------------------
  `load average`          Average number of       Compare with logical
                          runnable and            CPU count and
                          uninterruptible tasks   historical baseline; it
                          over 1, 5, and 15       is not CPU percentage
                          minutes                 

  `us`                    CPU time running        High values can
                          user-space code         indicate compute-heavy
                                                  application work

  `sy`                    CPU time in kernel      High values can
                          space                   indicate syscall,
                                                  networking, filesystem,
                                                  or kernel overhead

  `ni`                    CPU time running niced  Usually small;
                          user processes          interpret with workload
                                                  and priority

  `id`                    Idle CPU time           Low sustained idle time
                                                  can indicate CPU
                                                  pressure

  `wa`                    CPU time idle while I/O A clue to investigate
                          was outstanding         storage or other I/O;
                                                  not proof of disk
                                                  saturation

  `hi` / `si`             Hardware / software     Sustained high values
                          interrupt time          can indicate interrupt
                                                  or packet-processing
                                                  overhead

  `st`                    CPU time stolen by the  Relevant on virtualized
                          hypervisor              hosts; sustained steal
                                                  can reduce available
                                                  compute
  -----------------------------------------------------------------------

The exact presentation depends on the `top` version and configuration.
Press `1` to show per-CPU statistics on common procps-ng builds.

### Understand the process list

  Column        Meaning
  ------------- ----------------------------------------------------------
  `PID`         Process identifier
  `USER`        Process owner
  `PR` / `NI`   Scheduling priority and nice value
  `VIRT`        Virtual address space, not physical RAM consumption
  `RES`         Resident physical memory currently mapped by the process
  `SHR`         Shared resident memory estimate
  `S`           Process state
  `%CPU`        Recent CPU usage as reported by `top`
  `%MEM`        Resident memory as a fraction of physical memory
  `TIME+`       Accumulated CPU time
  `COMMAND`     Command name or command line, depending on configuration

Common process states include `R` (running or runnable), `S`
(interruptible sleep), `D` (uninterruptible sleep, often waiting on
I/O), `T` (stopped or traced), and `Z` (zombie). A process in `D` state
is not necessarily blocked on a local disk; network filesystems and
other kernel waits can also be involved.

### Useful interactive keys

-   `P` --- sort by CPU usage.
-   `M` --- sort by memory usage.
-   `1` --- toggle per-CPU views on common versions.
-   `H` --- toggle thread display.
-   `c` --- toggle command name / command line.
-   `u` --- filter by user.
-   `k` --- send a signal to a process. Use with care; do not kill
    processes just because they appear near the top.
-   `q` --- quit.

### Production interpretation

-   **One process consistently dominates CPU:** identify its workload,
    thread behavior, recent changes, and request volume. Confirm with
    interval samples rather than one refresh.
-   **Many processes consume CPU and idle time stays low:** suspect
    host-level CPU saturation or a capacity shortfall.
-   **High load with substantial CPU idle:** investigate uninterruptible
    tasks, storage/network filesystem waits, CPU affinity, and
    virtualization effects. Load average is not a CPU-utilization
    metric.
-   **High `wa`:** correlate with `iostat`, application latency, and the
    actual storage path before concluding that a disk is saturated.
-   **High `st`:** investigate noisy-neighbor or hypervisor capacity
    issues with the infrastructure team.

------------------------------------------------------------------------

## 3. `ps` --- point-in-time process inspection

### What it answers

`ps` takes a snapshot of process attributes. Unlike `top`, it does not
continuously refresh. It is useful for repeatable command-line queries,
sorting, filtering, process ancestry, and capturing evidence.

### High-value commands

``` bash
# Processes ranked by CPU
ps -eo pid,ppid,%cpu,%mem,cmd --sort=-%cpu | head -20

# Processes ranked by resident memory
ps -eo pid,ppid,%mem,rss,vsz,etime,cmd --sort=-rss | head -20

# Inspect one process
ps -p <PID> -o pid,ppid,user,stat,ni,pri,pcpu,pmem,rss,vsz,etime,args

# Show process tree
ps -ef --forest

# Show threads for a process
ps -T -p <PID> -o pid,tid,stat,pcpu,comm

# Find a process by command text
ps -ef | grep '[a]pp-name'
```

### Important columns

  -----------------------------------------------------------------------
  Column                  Meaning                 Caution
  ----------------------- ----------------------- -----------------------
  `PID` / `PPID`          Process ID / parent     Useful for ancestry and
                          process ID              identifying a
                                                  supervisor

  `%CPU`                  CPU utilization as      A snapshot-derived
                          calculated by `ps`      value; do not treat it
                                                  as a time series

  `%MEM`                  Resident memory as a    Does not indicate
                          percentage of physical  memory growth or a leak
                          RAM                     

  `RSS`                   Resident set size,      Shared pages can be
                          commonly reported in    counted in multiple
                          KiB                     processes; summing RSS
                                                  can overstate unique
                                                  physical use

  `VSZ`                   Virtual memory size,    Includes address space
                          commonly reported in    that may not be
                          KiB                     resident; not
                                                  equivalent to RAM use

  `STAT`                  Process state and       `D`, `Z`, and stopped
                          modifiers               states deserve
                                                  context-specific
                                                  investigation

  `ETIME`                 Elapsed time since      Not CPU time
                          process start           

  `NI` / `PRI`            Nice value / scheduling Priority changes can
                          priority                affect scheduling; do
                                                  not change blindly

  `CMD` / `ARGS`          Command name or full    May expose secrets
                          arguments               passed on command
                                                  lines; handle output
                                                  securely
  -----------------------------------------------------------------------

`%CPU` semantics and formatting vary by `ps` implementation and options.
On Linux procps, it is generally based on CPU time divided by elapsed
time since process start, so a short-lived spike can be diluted. Use
`top`, `pidstat`, or metrics for interval behavior.

### Process identity and ancestry

A high-resource process is not automatically the root cause. Establish:

-   Which service, deployment, container, or systemd unit owns it?
-   What is its parent process? Is it managed by systemd, a container
    runtime, or a supervisor?
-   Did its start time align with a deployment, traffic shift, scheduled
    job, or configuration change?
-   Is it one process with many threads, or many worker processes?
-   Is the PID still the same process? PIDs can be reused after a
    process exits.

Useful follow-up commands:

``` bash
# Executable and command line (may contain sensitive arguments)
readlink -f /proc/<PID>/exe
tr '\0' ' ' < /proc/<PID>/cmdline; echo

# Process limits, including open-file limit
cat /proc/<PID>/limits

# systemd unit properties
systemctl status <unit>
systemctl show <unit> --no-pager
```

Protect command output: process arguments, environment, paths, and unit
properties can contain sensitive information.

------------------------------------------------------------------------

## 4. `free` --- memory and swap overview

### What it answers

`free` summarizes physical memory and swap usage. It is a fast starting
point for determining whether the host has memory pressure, but it does
not identify which process is responsible or explain all kernel memory
behavior.

``` bash
free -h
free -h -w
free -m
```

`-h` uses human-readable units. `-w` separates buffers and cache on
supported procps versions.

### Understand the columns

  -----------------------------------------------------------------------
  Field                               Meaning
  ----------------------------------- -----------------------------------
  `total`                             Total memory visible to the command

  `used`                              Memory considered used by the
                                      `free` implementation

  `free`                              Completely unused memory

  `shared`                            Primarily shared memory such as
                                      tmpfs

  `buff/cache`                        Kernel buffers and reclaimable
                                      cache categories

  `available`                         Estimate of memory available for
                                      new applications without swapping
  -----------------------------------------------------------------------

The `used` calculation can differ between versions and display modes.
For operational decisions, **`available` is generally more useful than
`free`**. Linux intentionally uses otherwise-idle RAM for cache; a low
`free` value alone is not evidence of a problem.

### Example interpretation

``` text
               total        used        free      shared  buff/cache   available
Mem:            16Gi        9Gi         1Gi        500Mi       6Gi         6Gi
Swap:            2Gi        0B          2Gi
```

In this illustrative example, only 1 GiB is completely unused, but the
kernel estimates that 6 GiB is available. The host is not necessarily
under memory pressure.

### Swap interpretation

-   Non-zero swap usage does not automatically mean the system is
    currently thrashing. Pages may have been swapped out earlier and
    remain there.
-   Sustained swap-in (`si`) and swap-out (`so`) activity in `vmstat`,
    combined with low available memory and latency, is stronger evidence
    of active memory pressure.
-   Check swap activity, major page faults, memory PSI, OOM events, and
    application latency before taking action.

### Follow-up checks

``` bash
# Memory and swap summary
free -h

# Kernel memory counters
grep -E 'MemAvailable|SwapTotal|SwapFree|Dirty|Writeback|Slab|SReclaimable' /proc/meminfo

# OOM-related kernel messages (permissions and logging vary)
journalctl -k --since '30 min ago' | grep -i -E 'oom|out of memory|killed process'

# Per-process resident memory
ps -eo pid,ppid,%mem,rss,vsz,etime,cmd --sort=-rss | head -20
```

### Container and cgroup caution

A container can hit its memory limit while the node still has available
RAM. Inspect the container's cgroup memory limit, current usage, events,
and OOM counters. On cgroup v2 systems, relevant files commonly include
`memory.current`, `memory.max`, `memory.events`, and `memory.stat` under
the process's cgroup directory. Paths and visibility depend on the
runtime and mount configuration.

------------------------------------------------------------------------

## 5. `vmstat` --- system-wide activity and pressure clues

### What it answers

`vmstat` reports virtual-memory subsystem statistics along with
scheduler, CPU, swap, and block-I/O activity. It is especially useful
for determining whether the system is CPU-constrained, has runnable work
accumulating, or is experiencing memory and I/O pressure.

``` bash
vmstat 1 5
```

This requests five reports at one-second intervals. The first report is
commonly an average since boot; interpret subsequent reports as interval
samples.

### Understand the output

  -----------------------------------------------------------------------
  Group / field           Meaning                 Interpretation
  ----------------------- ----------------------- -----------------------
  `r`                     Runnable processes,     Compare with logical
                          including work          CPU count. A sustained
                          currently running       queue above available
                                                  CPU capacity can
                                                  indicate CPU contention

  `b`                     Processes in            Sustained values can
                          uninterruptible sleep   indicate tasks waiting
                                                  on I/O or another
                                                  kernel resource

  `swpd`                  Virtual memory in use   A quantity, not a
                                                  measure of current swap
                                                  activity

  `free`                  Idle memory             Do not use alone to
                                                  judge memory pressure

  `buff` / `cache`        Buffer and cache memory Context for memory
                                                  reclaimability

  `si` / `so`             Swap-in / swap-out rate Sustained activity can
                                                  indicate memory
                                                  pressure; units are
                                                  typically KiB/s on
                                                  Linux

  `bi` / `bo`             Blocks received from /  Activity indicators,
                          sent to block devices   not latency or
                                                  saturation measurements

  `in`                    Interrupts per second   Unexpectedly high rates
                                                  may point to device or
                                                  packet-processing
                                                  activity

  `cs`                    Context switches per    High values need
                          second                  workload context; they
                                                  are not inherently bad

  `us`                    User-space CPU time     Application computation

  `sy`                    Kernel-space CPU time   Kernel, syscall,
                                                  networking, filesystem
                                                  work

  `id`                    Idle CPU time           Sustained low idle can
                                                  indicate CPU pressure

  `wa`                    CPU time idle while I/O Correlate with device
                          was outstanding         latency and application
                                                  symptoms

  `st`                    Stolen CPU time         Relevant on virtualized
                                                  infrastructure
  -----------------------------------------------------------------------

### A practical interpretation sequence

1.  **Check `r` against CPU count.** Use `nproc` as a quick logical CPU
    count. A sustained run queue materially above available CPU capacity
    suggests contention, but CPU affinity, quotas, and workload shape
    matter.
2.  **Check `b` and `wa`.** If both rise, investigate blocked work and
    I/O paths. Do not assume the local disk is the cause.
3.  **Check `si` and `so`.** Sustained swap activity plus low memory
    availability suggests memory pressure.
4.  **Check `us` and `sy`.** High `us` often points toward application
    computation; high `sy` may indicate kernel overhead. Profile only
    when justified and safe.
5.  **Check `cs` and `in`.** Compare against baseline and workload. High
    rates can be normal for network-heavy or highly concurrent services.

### Useful commands

``` bash
nproc
vmstat 1 10
vmstat -w 1 10              # Wider output on supported versions
```

### Important limitations

-   `vmstat` is host-wide and can hide a single noisy container or
    cgroup.
-   `wa` is a CPU accounting state, not a direct disk-latency
    measurement.
-   `bi` and `bo` do not tell you which application caused the I/O.
-   A high context-switch rate is not automatically a performance
    defect.
-   For containerized workloads, inspect CPU quotas/throttling and
    cgroup memory pressure in addition to host-wide values.

------------------------------------------------------------------------

## 6. `iostat` --- CPU and storage-device performance

### What it answers

`iostat`, provided by the `sysstat` package on many Linux distributions,
reports CPU statistics and block-device I/O. Use extended statistics to
investigate throughput, IOPS, queueing, latency, and device utilization.

``` bash
iostat -xz 1 5
```

`-x` enables extended statistics, `-z` omits devices with no activity in
the sample, and `1 5` requests five one-second reports. The first report
commonly covers activity since boot; focus on later interval reports. If
supported, `iostat -y -xz 1 5` suppresses the first report.

### Important fields

  -----------------------------------------------------------------------
  Field                   Meaning                 Interpretation /
                                                  caution
  ----------------------- ----------------------- -----------------------
  `r/s`, `w/s`            Read and write requests IOPS; workload and
                          completed per second    device type determine
                                                  what is normal

  `rkB/s`, `wkB/s`        Read and write          Useful for bandwidth
                          throughput              analysis; field
                                                  names/units vary by
                                                  sysstat version

  `r_await`, `w_await`    Average time in         Compare with baseline,
                          milliseconds for        device type, workload,
                          read/write requests,    and application latency
                          including queueing and  
                          service time            

  `await`                 Average I/O request     A useful latency
                          wait time               signal, but not a
                                                  complete
                                                  application-latency
                                                  measure

  `aqu-sz`                Average queue length    Sustained growth can
                                                  indicate queueing;
                                                  interpret with device
                                                  and workload behavior

  `%util`                 Percentage of elapsed   Near 100% can indicate
                          time during which I/O   a busy device, but is
                          requests were issued to not a universal
                          the device              saturation measure for
                                                  parallel devices such
                                                  as modern SSDs and NVMe

  `rareq-sz`, `wareq-sz`  Average request size    Helps characterize I/O
                          for reads/writes        pattern

  `d/s`, `f/s`            Discard and flush       Relevant to storage
                          operations per second,  behavior and
                          where supported         filesystem/device stack
  -----------------------------------------------------------------------

Exact columns vary by sysstat version and platform. Check the local
`iostat(1)` manual for definitions and units.

### Read the signals together

-   **High IOPS and low latency:** the device is busy but may be
    handling the workload successfully.
-   **Rising `await` and rising `aqu-sz`:** requests are queueing or
    taking longer; investigate device limits, storage backend, and
    workload changes.
-   **High throughput with high latency:** bandwidth limits or large I/O
    operations may be involved.
-   **High `%util`:** evidence that the device is busy, not conclusive
    proof of saturation on highly parallel storage.
-   **Low local-device activity but application I/O latency:**
    investigate remote storage, network filesystems, database
    dependencies, filesystem locks, and application-level queues.

### Useful commands

``` bash
iostat -xz 1 10
iostat -d -x 1 5            # Device report
iostat -c 1 5               # CPU report
lsblk -o NAME,TYPE,SIZE,FSTYPE,MOUNTPOINTS
```

`iostat` reports block-device activity, not per-process attribution. Use
tools such as `pidstat -d`, `iotop` (if installed and permitted), or
application-level instrumentation when process-level attribution is
required. These tools may have privilege, overhead, or availability
constraints.

------------------------------------------------------------------------

## 7. Correlating the five commands

No single command proves a root cause. Combine signals and validate them
against service-level symptoms.

  ---------------------------------------------------------------------------
  Symptom           Start with        Correlate with     What to investigate
  ----------------- ----------------- ------------------ --------------------
  High CPU          `top`, `ps`       `vmstat` (`r`,     Hot process/thread,
                                      `us`, `sy`, `id`)  traffic increase,
                                                         inefficient code,
                                                         CPU quota/throttling

  High load average `top`             `vmstat` (`r`,     CPU queueing versus
                                      `b`, `wa`),        uninterruptible
                                      `iostat`           waits

  Low free memory   `free`            `ps` RSS, `vmstat` Available memory,
                                      (`si`, `so`)       reclaim, swap
                                                         activity, process
                                                         growth

  Suspected memory  `ps` repeated     `free`, cgroup     Per-process growth,
  leak              over time         metrics, OOM       workload
                                      events             correlation,
                                                         allocator/cache
                                                         behavior

  High I/O wait     `top`, `vmstat`   `iostat -xz`       Device latency,
                                                         queue depth, remote
                                                         storage, filesystem
                                                         behavior

  Slow application  `top`, `vmstat`   `iostat`,          Dependency latency,
  with normal host                    application        locks, network,
  CPU                                 metrics/traces     throttling,
                                                         connection pools

  Container is      Host commands as  cgroup/container   CPU quota, memory
  unhealthy but     context           metrics            limit, OOM kill, PID
  node looks fine                                        limit,
                                                         container-specific
                                                         pressure
  ---------------------------------------------------------------------------

### Scenario A: High CPU on a production node

1.  Confirm service impact and whether one node or the whole fleet is
    affected.
2.  Run `top` and identify high-CPU processes; use `top -H -p <PID>` if
    thread-level behavior matters.
3.  Use `ps` to capture process identity, parent, elapsed time, and
    resource ranking.
4.  Run `vmstat 1 6`; check whether the run queue is sustained and idle
    CPU is low.
5.  Check container CPU limits and throttling if the workload runs in a
    container.
6.  Correlate with traffic, request rate, latency, errors, and recent
    deployments.
7.  Mitigate based on evidence: roll back, reduce concurrency, shift
    traffic, or add capacity.

### Scenario B: Memory usage is increasing

1.  Start with `free -h`; focus on `available`, not only `free`.
2.  Rank processes by RSS with `ps`.
3.  Repeat snapshots over time; a single high RSS value does not
    establish a leak.
4.  Check `vmstat` for sustained swap-in/swap-out.
5.  Inspect cgroup memory limits/events and kernel OOM logs.
6.  Compare memory growth with traffic, cache size, worker count,
    deployment version, and uptime.
7.  If safe, use application allocation profiling. Mitigate first if the
    service is at risk.

### Scenario C: Application latency rises and I/O wait is high

1.  Confirm latency and error-rate impact at the service level.
2.  Check `top` and `vmstat` for `wa` and blocked tasks.
3.  Run `iostat -xz 1 6`; compare `await`, queue length, throughput, and
    `%util` with baseline.
4.  Identify the relevant device and storage path; map devices to mounts
    and backing storage.
5.  Check whether the dependency is local block storage, network
    storage, a database, or another remote service.
6.  Mitigate the workload or storage bottleneck; do not infer a disk
    failure from `wa` alone.

------------------------------------------------------------------------

## 8. Production troubleshooting checklist

-   [ ] What is the user-facing impact, and when did it begin?
-   [ ] Is the issue isolated to one process, container, node, or
    service fleet?
-   [ ] What changed recently: deployment, traffic, configuration,
    infrastructure, or dependency?
-   [ ] Have I captured more than one time-based sample?
-   [ ] Have I compared measurements with a known-good baseline?
-   [ ] Have I checked container/cgroup limits as well as host capacity?
-   [ ] Have I correlated host signals with application latency,
    throughput, and errors?
-   [ ] Is the next diagnostic action safe on a stressed production
    host?
-   [ ] Have I preserved relevant evidence without exposing secrets or
    sensitive command-line arguments?

### Commands to keep handy

``` bash
# CPU and process view
top
ps -eo pid,ppid,stat,%cpu,%mem,rss,etime,cmd --sort=-%cpu | head -20

# Memory
free -h
ps -eo pid,ppid,%mem,rss,vsz,etime,cmd --sort=-rss | head -20

# Scheduler, memory, and CPU activity
nproc
vmstat 1 6

# Storage
iostat -xz 1 6
lsblk -o NAME,TYPE,SIZE,FSTYPE,MOUNTPOINTS
```

------------------------------------------------------------------------

## 9. Hands-on exercises

Perform these in a disposable local VM or container, not on a production
host.

### Exercise 1 --- CPU-bound process

1.  Start a controlled CPU-bound process.
2.  Observe it with `top`.
3.  Rank processes with `ps`.
4.  Run `vmstat 1 10` and compare `r`, `us`, `id`, and `cs`.
5.  Limit the container's CPU quota and observe the difference between
    host CPU utilization and container CPU throttling.
6.  Explain whether the workload is using all host CPU, exhausting its
    quota, or both.

### Exercise 2 --- Memory behavior

1.  Observe `free -h` before and after a controlled memory allocation.
2.  Compare `MemFree`, `MemAvailable`, and `buff/cache`.
3.  Observe the process RSS using `ps`.
4.  If using a container, set a safe memory limit in a disposable
    environment and inspect cgroup memory events.
5.  Explain why high RSS or low `MemFree` alone does not prove a leak.

### Exercise 3 --- Storage behavior

1.  In a disposable environment, generate a controlled I/O workload.
2.  Observe it with `iostat -xz 1 10`.
3.  Compare IOPS, throughput, `await`, `aqu-sz`, and `%util`.
4.  Change the workload's read/write pattern and compare the results.
5.  Explain why `%util` alone is insufficient to declare modern SSD/NVMe
    storage saturated.

------------------------------------------------------------------------

## 10. Senior SRE interview questions

Try answering each question aloud before reviewing the key points.

### Q1. Load average is 20 on a 16-vCPU host. Is the host overloaded?

**Strong answer:** It may be under pressure, but load average is not CPU
utilization. It includes runnable tasks and tasks in uninterruptible
sleep. I would inspect `vmstat` (`r` and `b`), CPU idle and I/O wait,
per-process state, and the workload's CPU affinity or cgroup quota. I
would also compare against the host's baseline and service-level
symptoms. A load average above 16 is a clue, not a diagnosis.

### Q2. `free` reports only 300 MiB free on a 32 GiB host. Should you add memory?

**Strong answer:** Not from that number alone. Linux uses memory for
cache. I would inspect `MemAvailable`, swap-in/swap-out activity, memory
pressure, OOM events, and application/cgroup limits. Low `MemFree` with
healthy `MemAvailable` and no pressure may be normal.

### Q3. A process has high RSS. Is it a memory leak?

**Strong answer:** Not necessarily. RSS includes resident pages and may
include shared mappings; it is not a measure of growth. I would track
the process over time under comparable load, compare versions and worker
counts, inspect cgroup memory and OOM events, and distinguish heap
growth from caches, memory-mapped files, and allocator retention. If
safe, I would use application-level allocation profiling. I would
mitigate risk before running invasive diagnostics.

### Q4. `vmstat` shows high `wa`. Does that prove the disk is saturated?

**Strong answer:** No. `wa` indicates CPU time idle while I/O was
outstanding; it does not identify the device or prove saturation. I
would correlate with `iostat` latency, queue length, throughput, and
device utilization, then investigate the full I/O path, including
network storage and remote dependencies.

### Q5. `iostat` reports 100% `%util` on an NVMe device. Is it saturated?

**Strong answer:** Not necessarily. `%util` describes time with I/O
issued and is not a universal saturation metric for devices capable of
parallel processing. I would examine latency (`await`), queue depth,
IOPS, throughput, device-specific limits, and application latency, and
compare with a known-good baseline.

### Q6. The node has healthy CPU and memory, but a Kubernetes workload is slow. What next?

**Strong answer:** Host health does not guarantee container health. I
would inspect pod CPU and memory requests/limits, CPU throttling, cgroup
memory events, restarts/OOM kills, PID limits, and per-container
metrics. Then I would correlate traces and application metrics with
dependency latency, network behavior, and recent deployments.

### Q7. Why use both `ps` and `top`?

**Strong answer:** `top` provides a live, continuously refreshed view
and is useful for observing changing behavior. `ps` provides a
scriptable point-in-time snapshot that is easy to sort, filter, and
capture. I use them together to identify a candidate process and then
establish its identity, ancestry, state, and resource profile.

### Q8. What would you do first on a severely degraded production host?

**Strong answer:** Establish impact and preserve a minimal baseline
using low-overhead, read-only commands. I would avoid broad tracing,
profilers, large dumps, or repeated expensive scans. I would determine
whether the issue is host-wide or isolated to a workload, correlate
resource signals with service metrics, and choose a reversible
mitigation. Diagnostics should be proportional to the risk and performed
under the incident process.

------------------------------------------------------------------------

## 11. Common mistakes and interview traps

-   Treating load average as CPU percentage.
-   Treating `MemFree` as the only meaningful memory metric.
-   Calling high RSS a memory leak without proving growth over time.
-   Treating non-zero swap usage as proof of active swapping.
-   Treating `wa` as a direct disk-saturation metric.
-   Treating `%util = 100` as conclusive saturation on NVMe or other
    parallel devices.
-   Treating one `ps` or `top` snapshot as proof of a sustained trend.
-   Ignoring cgroup CPU and memory limits because the host looks
    healthy.
-   Running invasive diagnostics on a stressed production host without
    assessing overhead and approval.
-   Sharing raw process arguments or logs without checking for secrets.

------------------------------------------------------------------------

## 12. Further reading

Use the manual pages installed on the system as the source of truth for
local command options and output:

``` bash
man top
man ps
man free
man vmstat
man iostat
```

Useful official references:

-   [procps-ng documentation](https://gitlab.com/procps-ng/procps)
-   [sysstat project](https://github.com/sysstat/sysstat)
-   [Linux kernel documentation](https://docs.kernel.org/)
-   [Linux pressure stall information
    (PSI)](https://docs.kernel.org/accounting/psi.html)
-   [Control group v2
    documentation](https://docs.kernel.org/admin-guide/cgroup-v2.html)

**Core principle:** identify the symptom, measure over time, correlate
independent signals, inspect the correct resource boundary, and validate
the suspected cause before changing production.
