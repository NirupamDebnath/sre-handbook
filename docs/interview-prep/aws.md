# AWS and EKS interview bank

1. **AccessDenied after role assumption?** Verify caller/role/session, action/resource/context; inspect identity/resource policy, boundaries, SCPs, and explicit denies.
2. **Private workload cannot reach internet.** Trace subnet route, NAT route/AZ design, security group/NACL, DNS, and egress proxy policy.
3. **IRSA vs Pod Identity?** Both deliver workload AWS credentials; IRSA uses OIDC federation, Pod Identity uses EKS associations/agent. Choose per current platform constraints and least privilege.
4. **EKS node NotReady?** Preserve events/kubelet/runtime/CNI evidence; check resource/disk/network/IAM; cordon and replace through managed capacity if warranted.
5. **Pods cannot get IPs.** Verify CNI errors, subnet capacity, ENI/IP limits, prefix delegation configuration, and scheduling pattern.
6. **Upgrade strategy?** Verify version matrix/add-ons, rehearse, upgrade control plane, roll nodes, validate workloads and rollback/contingency.
7. **Multi-AZ design?** Spread stateless capacity and dependencies across AZs, test AZ loss, understand data replication and cross-AZ cost.
8. **EBS vs EFS?** EBS is block storage typically attached per volume/AZ constraints; EFS is shared file storage with different performance/semantics. Select from workload requirements.
9. **Cloud cost suddenly rises.** Attribute with tags/Cost Explorer, correlate usage/resource changes, confirm anomaly, apply safe right-sizing/lifecycle controls.
10. **DR plan?** Define RTO/RPO, backups/replication, dependencies, failover authority, test restore/failover, and document data consistency trade-offs.
