# Kubernetes interview bank

1. **Pod Pending?** Read events; test requests/capacity, taints, affinity, quotas, PVC binding, and autoscaler constraints.
2. **CrashLoopBackOff?** Inspect current/previous logs, exit code, OOM, config, probes, and dependency behavior; stop harmful restart changes.
3. **ImagePullBackOff?** Verify exact image/tag/digest, registry access, pull credentials, DNS/network, and architecture.
4. **DNS failure?** Test from the Pod, inspect resolver config, Service/endpoints, CoreDNS health/logs, network policy, and upstream DNS.
5. **Readiness vs liveness?** Readiness gates traffic; liveness restarts stuck processes. A dependency check as liveness can amplify outage.
6. **PDB trade-off?** It protects availability during voluntary disruption but may block drains/upgrades if impossible to satisfy.
7. **HPA not scaling?** Check metric availability, targets, requests, stabilization behavior, min/max, and whether nodes can schedule replicas.
8. **Secure a workload?** Dedicated service account/RBAC, restricted security context, image policy, network policy, secret manager, and admission controls.
9. **Rollback failed rollout?** Pause, assess impact, undo to known good revision, validate SLI, preserve artifacts, then investigate.
10. **API server latency?** Examine control-plane metrics/audit and client behavior, object churn/watch load, admission webhooks, and provider support path.
