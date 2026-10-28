# Scenario-based investigations

Use this answer structure: symptoms and impact; initial triage; commands/evidence; hypotheses; root cause (only once proved); immediate mitigation; long-term actions; prevention/monitoring; follow-ups.

## Pods stuck Pending

**Symptoms and impact:** new replicas remain Pending; capacity or availability may be reduced. **Triage/evidence:** inspect `kubectl describe pod`, events, requests, quota, node labels/taints, PVCs, and autoscaler status. **Hypotheses:** insufficient requested resources, unsatisfied affinity/taint, quota, unbound storage, or capacity that cannot scale.

**Mitigation:** restore a schedulable configuration or add approved capacity; do not simply remove all requests. **Root cause:** state it only after events/config/capacity prove it. **Prevention:** admission checks, capacity headroom, dashboards for Pending reasons, and deployment preflight. **Follow-up:** How would a strict topology rule change your answer?

## CrashLoopBackOff

Collect previous logs, exit code, OOM/probe events, config/secret version, and rollout timing. Test application startup, dependency reachability, command/args, and resource limit hypotheses. Pause rollout or restore known-good config when it reduces harm; preserve evidence. Prevent with startup probes, config validation, realistic limits, and canary checks. Follow-up: when would you scale down rather than restart?

## DNS failures in Kubernetes

Measure affected namespaces/nodes and use an ephemeral approved debug Pod to query service and external names. Inspect Pod `resolv.conf`, Service/endpoints, CoreDNS health/logs, network policies, node DNS path, and upstream resolver. Mitigate the confirmed failing component or route; prevent with DNS SLI and capacity/config tests. Follow-up: why might one application fail while others work?

## Latency and 5xx after deployment

Compare SLO, traffic, errors, and latency by revision; trace a slow/error request; inspect logs and dependency saturation. Hypotheses include bad config, incompatible schema, resource throttling, retry amplification, or dependency regression. Pause/rollback if the prior version is safe, validate recovery, then fix tests and rollout guardrails. Follow-up: when is rollback unsafe because of a migration?

## EKS worker nodes NotReady

Scope nodes/AZs, inspect node conditions/events, kubelet/runtime/CNI logs, resource pressure, cloud instance health, and network/IAM dependencies. Cordon to protect scheduling; drain only when disruption budgets and availability permit; replace proven unhealthy capacity. Add node-health dashboards, upgrade rehearsals, and spare capacity. Follow-up: what evidence makes this a control-plane issue instead?

## Pod IP exhaustion

Check CNI allocation errors, free subnet addresses, instance limits, CNI/prefix configuration, and workload density. Add supported capacity or tune a validated CNI design; do not change network settings blind during an incident. Track IP headroom and forecast deployment demand. Follow-up: what changes under dual-stack networking?

## Prometheus targets disappear

Inspect target labels/status/error, service discovery, relabel rules, TLS/auth, network path, and Prometheus resource saturation. Restore the proven discovery/config/endpoint path; do not silence the alert without preserving detection. Monitor scrape health and config rollout. Follow-up: how do you avoid alert storms when Prometheus itself is impaired?

## Argo CD sync failure

Read application conditions, rendered diff, repository revision, project permissions, cluster credentials, hooks, and resource health. Correct the Git desired state or access/config issue, then sync with a reviewed scope. Avoid prune/force during ambiguity. Prevent with render/schema/policy checks in CI. Follow-up: how do you reconcile a necessary emergency hotfix?

## AWS permission error

Record request ID, principal, assumed-role session, action/resource, and region. Evaluate identity/resource policies, boundaries, SCPs, session policies, and explicit denies. Apply the smallest tested policy change; avoid broad administrator grants. Add policy tests and clear access ownership. Follow-up: why can `get-caller-identity` succeed while the action fails?

## Terraform state conflict

Stop concurrent writers, identify the lock holder and intended revision, and inspect backend/state health. Never force-unlock without proving the holder is stale. Replan from the current state, apply serialized change, then improve CI locking and ownership. Follow-up: how do you handle an emergency manual change made during the lock?
