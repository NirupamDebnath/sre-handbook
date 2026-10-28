# SRE principles

SRE applies software engineering to operations. DevOps is the broader cultural and delivery practice; SRE supplies concrete reliability mechanisms such as service-level objectives, error budgets, automation, and incident learning.

## Core ideas

- **Service ownership:** a team owns the user outcome, including operability and failure recovery.
- **Toil:** manual, repetitive, automatable work with no enduring value. Reduce it with safe automation, not merely faster clicking.
- **Risk budgets:** perfect availability is rarely rational; choose a target that balances user harm, cost, and delivery speed.
- **Blameless learning:** investigate system conditions and decisions, not individual fault. Accountability still means completing corrective actions.

### Exercise

List recurring operational work for one service. For each item record frequency, time, failure risk, and automation boundary. Automate only after defining input validation, least privilege, idempotency, rollback, and an audit trail.

## Interview prompt

**How would you reduce toil without increasing risk?** Baseline hours and failure rate first. Prioritize high-frequency, rule-based work; automate one narrow path behind approvals and observability; measure time saved and failed executions. Keep an escape hatch and use the saved capacity to remove the underlying cause.
