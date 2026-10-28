# Linux troubleshooting

Start with impact, process identity, and a short baseline; do not run invasive commands blindly on a stressed host.

| Question | Command | Interpretation / caution |
|---|---|---|
| Which process consumes resources? | `ps -eo pid,ppid,%cpu,%mem,cmd --sort=-%cpu` | A point-in-time ranking; correlate with time series. |
| Is the host runnable or I/O bound? | `vmstat 1 5` | `r` suggests runnable work; `wa` suggests I/O wait. Compare to CPU count. |
| Are disks saturated? | `iostat -xz 1 3` | High await/util needs workload and device context. |
| Who holds a port/file? | `ss -ltnp`; `lsof -p PID` | Process details may require privilege; avoid exposing sensitive paths. |
| What did the unit report? | `journalctl -u app --since '15 min ago'` | Time-box output and preserve it with access controls. |

## Investigation path

Confirm whether the problem is host-wide or one cgroup/container. Check limits (`systemctl show`, cgroup metrics), file descriptors (`/proc/PID/limits`), and recent deploys. `strace -p PID` can reveal blocking syscalls but adds overhead and often requires elevated privilege—use briefly and only with approval.

## Exercise

Run a controlled CPU-bound process in a local container; observe it with `ps`, `top`, and `vmstat`. Set a container CPU limit and compare throttling metrics instead of assuming host CPU tells the full story.

## Interview question

**A process has high memory; is it a leak?** Not necessarily. Separate RSS, page cache, allocator behavior, and cgroup limit/oom events. Graph growth across deployments and load, inspect allocation profiling if safely available, and mitigate by limiting concurrency or rolling back before declaring a leak.
