# Linux

Linux is the foundation of most production infrastructure. Senior SREs
need to understand process behavior, resource management,
operating-system performance, and practical troubleshooting---not just
command syntax.

## Learning path

  -----------------------------------------------------------------------
  Topic                               What to learn
  ----------------------------------- -----------------------------------
  Processes and threads               Process lifecycle, PID/PPID,
                                      signals, states, threads,
                                      scheduling

  CPU and scheduling                  Load average, run queues, CPU
                                      states, context switches, CPU
                                      quotas

  Memory management                   Virtual memory, RSS, page cache,
                                      swap, OOM behavior, cgroups

  Storage and filesystems             Block I/O, filesystem capacity,
                                      latency, inodes, mounts

  Linux networking                    Sockets, ports, connection states,
                                      routing, DNS, packet
                                      troubleshooting

  Performance troubleshooting         Establishing baselines, correlating
                                      metrics, isolating bottlenecks
  -----------------------------------------------------------------------

## Practical command guides

  ----------------------------------------------------------------------------
  Guide                                    Description
  ---------------------------------------- -----------------------------------
  [Linux Performance Monitoring and        A practical reference for `top`,
  Troubleshooting](system-monitoring.md)   `ps`, `free`, `vmstat`, and
                                           `iostat`, including output
                                           interpretation, production
                                           scenarios, exercises, and Senior
                                           SRE interview questions.

  ----------------------------------------------------------------------------

## Linux troubleshooting

Start with impact, process identity, and a short baseline; do not run
invasive commands blindly on a stressed host.

  ----------------------------------------------------------------------------------------------
  Question                Command                                        Interpretation /
                                                                         caution
  ----------------------- ---------------------------------------------- -----------------------
  Which process consumes  `ps -eo pid,ppid,%cpu,%mem,cmd --sort=-%cpu`   A point-in-time
  resources?                                                             ranking; correlate with
                                                                         time series.

  Is the host runnable or `vmstat 1 5`                                   `r` suggests runnable
  I/O bound?                                                             work; `wa` suggests I/O
                                                                         wait. Compare with CPU
                                                                         count and other
                                                                         evidence.

  Are disks saturated?    `iostat -xz 1 3`                               High `await`, queue
                                                                         depth, or `%util` needs
                                                                         workload and device
                                                                         context.

  Who holds a port/file?  `ss -ltnp`; `lsof -p PID`                      Process details may
                                                                         require privilege;
                                                                         avoid exposing
                                                                         sensitive paths.

  What did the unit       `journalctl -u app --since '15 min ago'`       Time-box output and
  report?                                                                preserve it with access
                                                                         controls.
  ----------------------------------------------------------------------------------------------

## Investigation path

Confirm whether the problem is host-wide or isolated to one
cgroup/container. Check limits (`systemctl show`, cgroup metrics), file
descriptors (`/proc/PID/limits`), and recent deployments.
`strace -p PID` can reveal blocking syscalls but adds overhead and often
requires elevated privilege---use briefly and only with approval.

## Exercises

Run a controlled CPU-bound process in a local container; observe it with
`ps`, `top`, and `vmstat`. Set a container CPU limit and compare
throttling metrics instead of assuming host CPU tells the full story.

Use the [Linux performance monitoring guide](system-monitoring.md) for
memory and storage exercises as well.

## Interview question

**A process has high memory; is it a leak?**

Not necessarily. Separate RSS, page cache, allocator behavior, and
cgroup limit/OOM events. Graph growth across deployments and load,
inspect allocation profiling if safely available, and mitigate by
limiting concurrency or rolling back before declaring a leak.
