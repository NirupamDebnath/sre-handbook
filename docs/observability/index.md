# Observability

Metrics quantify trends and alert conditions; logs provide event detail; traces connect work across boundaries; events describe changes. Instrument a user journey with stable service/environment attributes and propagate trace context through calls.

## Investigation example

Latency rises after a rollout. First graph RED signals (rate, errors, duration) by revision and endpoint. Trace slow requests to locate the waiting dependency. Query correlated structured logs using trace ID, then compare saturation (USE: utilization, saturation, errors) for the implicated resource. A high-cardinality label such as user ID can make Prometheus expensive or unstable; aggregate or move that dimension to logs/traces.

```promql
histogram_quantile(0.99,
  sum by (le, route) (rate(http_request_duration_seconds_bucket[5m])))
```

Use recording rules for expensive, repeatedly-used queries. Sample traces intentionally; tail sampling can retain errors/slow traces but requires collector capacity. Define retention and cardinality budgets.

## Alert design

Page on user impact with a responder action; route causes and trends to tickets/dashboards. Include service, owner, runbook, dashboard, severity, and deduplication keys. Prometheus target disappearance may be service discovery, network/TLS/auth, scrape config, relabeling, or Prometheus capacity—inspect target status and logs before blaming the target.

Further reading: [Prometheus docs](https://prometheus.io/docs/introduction/overview/) and [OpenTelemetry docs](https://opentelemetry.io/docs/).
