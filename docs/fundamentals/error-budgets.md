# Error budgets and burn-rate alerts

An error budget is the permitted unreliability implied by an SLO. It creates a shared decision rule: when consumption is normal, deliver; when it is exhausted, prioritize reliability work.

For a 99.9% 30-day availability SLO, the budget is 0.1%. A 14.4× burn rate spends a full 30-day budget in about 50 hours. Alert on both a fast and slow window to catch acute and persistent harm while rejecting short spikes.

```promql
# Illustrative: bad-event ratio over 5 minutes
sum(rate(http_requests_total{code=~"5.."}[5m]))
/ sum(rate(http_requests_total[5m]))
```

## Multi-window policy

| Signal | Example action | Why |
|---|---|---|
| High burn in 5m and 1h | Page | Immediate user risk with confirmation. |
| Moderate burn in 30m and 6h | Ticket/urgent review | Sustained degradation. |
| Budget trending down | Capacity/reliability planning | Prevent the page. |

Tune thresholds from historical traffic and incident data. Include low traffic safeguards; a single error can distort a ratio.

## Exercise

Choose an API, define the denominator and “good” event, calculate the allowed failures for a 28-day window, and write a page condition that requires a short and long window. Test it against a known benign burst.
