# Hands-on labs

Run labs in a disposable local environment first. Cloud labs can incur charges; inspect a plan and type an explicit confirmation before creating or deleting resources.

| Lab | Difficulty / time | Outcome |
|---|---|---|
| Local Kubernetes troubleshooting | Intermediate / 75 min | Diagnose scheduling, probes, and resource pressure. |
| Helm release | Intermediate / 60 min | Render, validate, and roll back a chart. |
| Prometheus, Grafana, logs and traces | Intermediate / 2 h | Follow a slow request across telemetry. |
| Argo CD workflow | Advanced / 90 min | Observe reconciliation and intentional drift. |
| Terraform AWS baseline | Intermediate / 90 min | Plan and clean up a minimal tagged environment. |
| SLO alert | Advanced / 75 min | Test a multi-window, actionable signal. |
| AI incident summary | Advanced / 2 h | Build a read-only, citation-based prototype. |
| Network fault diagnosis | Intermediate / 60 min | Isolate DNS, TLS, and TCP failures. |
| Resource-pressure diagnosis | Intermediate / 60 min | Separate CPU throttling, memory OOM, and I/O wait. |
| Distributed tracing | Advanced / 90 min | Propagate trace context and validate sampling. |

## Lab: local Kubernetes application

**Prerequisites:** Docker, `kind` or `minikube`, `kubectl`; use a disposable cluster. **Architecture:** client → Service → Deployment.

```bash
kind create cluster --name sre-lab
kubectl apply -f app.yaml             # create this from the Kubernetes guide
kubectl rollout status deploy/api
kubectl get pods,svc
```

Set an intentionally impossible CPU request in a copy of the manifest and inspect `kubectl describe pod`. Then set a bad readiness path, observe endpoints stay unavailable, and restore it. Expected evidence is a scheduler event in the first case and readiness failures in the second. Clean up with `kind delete cluster --name sre-lab`; this deletes that local cluster only.

## Lab: deployment safety

**Prerequisites:** a local cluster and metrics/log access. Deploy three replicas with a PDB and rolling strategy, introduce a failing revision to one replica, observe readiness and error rate, then pause/undo:

```bash
kubectl rollout pause deployment/api
kubectl rollout undo deployment/api
kubectl rollout status deployment/api
```

Validate the user-path SLI, not merely replica count. Record what trigger would have halted the rollout automatically.

## Lab: Helm, GitOps, and observability

**Prerequisites:** local cluster, Helm, and (for GitOps) a disposable Argo CD installation. Create a chart with a Deployment, Service, requests/limits, and probes. Run `helm lint`, `helm template`, and a server-side dry run before installation. Change one value, inspect `helm diff` if your environment has the plugin, and use `helm rollback` to a known release after validation. For GitOps, commit the rendered desired change, let Argo CD report the diff, sync only the reviewed application, and deliberately make then reconcile a harmless label drift.

Install Prometheus/Grafana in the same disposable cluster using their maintained charts or a local stack. Create a counter, a latency histogram, structured logs with a request ID, and a trace span in a sample service. Generate a controlled slow request; verify the metric dashboard leads to trace and log evidence. Remove the namespace/releases afterward; confirm no shared context is targeted.

## Lab: network and resource fault diagnosis

**Prerequisites:** a disposable container/cluster. Break a test name mapping or route in an isolated test and compare `dig`, `curl -v`, and `ss` output. Restore the path and write which protocol layer each signal proved. For resource pressure, run bounded CPU, memory, and disk-I/O test workloads one at a time; collect `vmstat`, `iostat`, cgroup/container metrics, and termination events. Validation is distinguishing the three mechanisms from evidence, not merely observing slowness. Delete only the explicitly-created local cluster/containers.

## Lab: Terraform-managed AWS baseline

**Prerequisites:** an approved sandbox AWS account, budget alert, least-privilege role, Terraform. Create only tagged resources in an isolated module. Run `terraform plan -out=tfplan`, review every action, then apply only after an intentional approval. Confirm tags and cost visibility. Cleanup is `terraform destroy` **only after** reviewing its full plan and confirming the workspace contains only lab resources; it deletes managed resources in that state.

## Lab: AI-assisted incident summary

Use a synthetic incident timeline and approved local/read-only corpus. Build output fields for impact, timeline, cited evidence, unknowns, and suggested checks. Test with contradictory evidence and injected instructions. Validation means every claim is either cited or marked uncertain; no command executes without a human approval boundary.
