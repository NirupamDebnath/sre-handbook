# Incident management

## Response lifecycle

1. Confirm impact, scope, and affected journey; create an incident record.
2. Assign an incident commander, operations lead, and communications owner as scale requires.
3. Stabilize using the smallest reversible mitigation: pause rollout, shed noncritical load, fail over, or roll back.
4. Continue evidence collection separately from mitigation; timestamps matter.
5. Close with a blameless review: conditions, detection gaps, decisions, corrective actions, and owners/dates.

## Operational readiness

Pages must be actionable: a user-impact signal, a runbook link, ownership, severity criteria, and a tested escalation path. Avoid paging on every symptom; route non-urgent capacity trends to a working queue.

## Interview prompt

**A rollback restores service but the root cause is unclear. What next?** Preserve artifacts and timelines, verify recovery against the SLI, keep heightened monitoring, communicate residual risk, and schedule an investigation. Do not redeploy the suspected version simply to “see if it happens again.”
