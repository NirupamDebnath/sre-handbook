# Linux interview bank

1. **Load average is high; what next?** Compare runnable work and CPU count with `vmstat`, then process CPU, I/O wait, and blocked tasks. Load alone cannot diagnose CPU exhaustion.
2. **A service cannot open files.** Inspect per-process limits, current descriptors, leaks, and system-wide limits with `lsof`/`/proc`; raise limits only with capacity and leak analysis.
3. **OOMKilled container?** Confirm cgroup limit and events, RSS growth, requests/limits, and node pressure; mitigate by rollback or bounded memory/concurrency, then profile.
4. **Disk is full but `du` disagrees.** Look for deleted-but-open files with `lsof +L1`, inode exhaustion, mounts, and log rotation behavior.
5. **How do signals affect shutdown?** SIGTERM requests graceful exit; SIGKILL cannot be handled. Ensure PID 1 forwards signals and termination grace fits drain time.
6. **High iowait?** Correlate device latency/utilization, queue depth, workload, and remote storage; do not infer a disk fault from iowait alone.
7. **systemd service flaps.** Read unit status/journal, exit codes, restart policy, dependencies, limits, and recent config changes.
8. **CPU limit hurts latency.** Compare throttling, queueing, requests, and actual demand; tune only after load testing.
9. **Safe use of strace?** Attach briefly with approval, target one PID, understand overhead/privacy, and use syscall evidence to refine a hypothesis.
10. **What is operationally useful logging?** Timestamped structured events with request/correlation IDs, level discipline, redaction, retention, and a documented query path.
