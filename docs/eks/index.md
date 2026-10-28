# Amazon EKS operations

EKS manages the Kubernetes control plane; worker capacity, add-ons, networking, and workload configuration remain shared responsibilities. Plan Kubernetes-version upgrades with compatibility checks, a staging rehearsal, control-plane upgrade, add-on updates, and node replacement/rollout strategy. Consult the current [EKS documentation](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html) for supported versions.

## Workload identity

IRSA uses an IAM OIDC provider and service-account token projection to obtain AWS credentials. EKS Pod Identity associates IAM roles with service accounts through the EKS agent and removes some OIDC-provider administration. Both require least-privilege IAM policy and should be tested from the workload; neither turns Kubernetes RBAC into IAM authorization.

## Pod IP pressure

With the Amazon VPC CNI, Pods commonly consume VPC IP addresses. Symptoms include Pods Pending or CNI allocation errors. Collect CNI logs/events, node/pod counts, subnet free addresses, CNI configuration, and instance ENI/IP limits. Mitigations may include adding address capacity, choosing supported prefix delegation settings, or changing node design—validate against the current [VPC CNI guide](https://docs.aws.amazon.com/eks/latest/best-practices/prefix-mode-linux.html).

## Node NotReady

Differentiate kubelet, runtime, CNI, DNS, IAM, disk/memory pressure, and network reachability. Cordon before disruptive action when safe, preserve logs, then replace unhealthy immutable capacity through its managed mechanism.
