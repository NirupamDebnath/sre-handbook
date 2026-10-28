# Observability interview bank

1. **Metrics, logs, traces?** Metrics detect/quantify, logs explain events, traces connect request work; use them together.
2. **RED vs USE?** RED focuses service request rate/errors/duration; USE focuses resource utilization/saturation/errors.
3. **Cardinality incident?** Identify explosive labels, stop new series, aggregate/drop unsafe dimensions, and protect query/ingestion capacity.
4. **Target disappeared?** Inspect Prometheus targets/discovery/relabeling, network/TLS/auth, target metrics endpoint, and Prometheus resources.
5. **Missing traces?** Verify SDK/exporter, context propagation, collector pipeline, sampling policy, backend ingestion, and clock/attribute consistency.
6. **p99 rose but average is stable.** Segment by route/revision/region and inspect histogram buckets/traces; tail behavior can harm users despite a stable mean.
7. **Recording rules?** Precompute frequent expensive PromQL for dashboards/alerts while preserving raw signals needed for investigation.
8. **Alert is noisy.** Quantify false/low-action pages, improve user-impact condition and multi-window confirmation, route non-pages appropriately.
9. **Logs are expensive.** Define retention/tiering, sample verbose successes, redact early, and preserve security/audit needs.
10. **Dashboard design?** Begin with user journey and SLO, then dependency and resource drill-downs; include deploy annotations and ownership.
