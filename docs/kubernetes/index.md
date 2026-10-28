# Kubernetes operations

## Workload and scheduling model

A Deployment manages stateless ReplicaSets; StatefulSets give stable identity/storage ordering; DaemonSets run one Pod per eligible node; Jobs and CronJobs run bounded work. The scheduler evaluates requests, taints/tolerations, affinity, topology constraints, and available nodes—not limits alone.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata: {name: api}
spec:
  replicas: 3
  strategy: {type: RollingUpdate, rollingUpdate: {maxUnavailable: 0, maxSurge: 1}}
  selector: {matchLabels: {app: api}}
  template:
    metadata: {labels: {app: api}}
    spec:
      containers:
        - name: api
          image: nginx:1.27
          resources: {requests: {cpu: 100m, memory: 128Mi}, limits: {memory: 256Mi}}
          readinessProbe: {httpGet: {path: /, port: 80}, initialDelaySeconds: 3}
```

Readiness controls traffic eligibility; liveness restarts a stuck process; startup probes protect slow boot. Misusing liveness for a temporarily unavailable dependency can create a restart storm.

## Triage

`kubectl get events --sort-by=.lastTimestamp`, `kubectl describe pod POD`, `kubectl logs POD -c CONTAINER --previous`, and `kubectl get nodes` build a timeline. Check Pending for scheduling events, CrashLoopBackOff for exit/oom/probe evidence, and ImagePullBackOff for image reference, registry reachability, and authorization.

## Production decisions

Use PDBs with care: overly strict budgets can block node drain. HPA needs meaningful metrics; Cluster Autoscaler/Karpenter need schedulable capacity. Restrict RBAC, apply Pod Security standards/security contexts, and keep Secrets out of Git.
