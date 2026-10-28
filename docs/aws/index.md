# AWS foundations

## Identity and networking

Use IAM roles and STS temporary credentials rather than long-lived access keys. Scope policies to actions, resources, and conditions; test intended and denied paths. A VPC spans an AWS Region; subnets live in one Availability Zone. Route tables, security groups, network ACLs, DNS, and load balancers form a request path that must be debugged end to end.

## Practical evidence

```bash
aws sts get-caller-identity                 # confirms active principal, not authorization
aws iam simulate-principal-policy --policy-source-arn ARN --action-names s3:GetObject
```

The simulator has limits and does not replace testing resource policies, SCPs, permission boundaries, session policies, or service-specific context. Avoid broad `*` permissions as a troubleshooting shortcut.

## Reliability and cost

Distribute critical paths across AZs, understand managed-service failure modes, set backups and restoration tests to RPO/RTO, and use tags/budgets to expose ownership. Multi-region adds latency, data consistency, and operational complexity; justify it with a tested recovery objective.

See [AWS IAM documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) and [Amazon VPC documentation](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html).
