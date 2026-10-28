# Security for SRE work

Reliability and security reinforce each other: least privilege limits blast radius, controlled changes improve recovery, and audit trails make incidents diagnosable. Use workload identity instead of static credentials; rotate and scope secrets; encrypt in transit and at rest; segment networks; patch base images and dependencies.

For Kubernetes, apply RBAC by namespace/verb/resource, use dedicated service accounts, default-deny network policies where supported, drop Linux capabilities, run as non-root, and restrict admission of risky workloads. Secret encoding is not encryption; use an approved secret manager and redact telemetry.

**Trade-off:** emergency access needs fast recovery but cannot become a permanent bypass. Time-bound, audited break-glass access plus post-use review provides a safer boundary.
