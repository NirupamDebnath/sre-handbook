# SLIs, SLOs, and SLAs

An **SLI** is a measured indicator of a user-relevant outcome. An **SLO** is the target for that indicator over a window. An **SLA** is an external commitment with consequences; it should be no more ambitious than the internal SLO.

## Build a useful availability SLI

For a checkout API, count successful, valid requests over eligible requests:

```text
availability = good events / valid events
```

If the 30-day SLO is 99.9%, the monthly error budget is 0.1%. For 1,000,000 valid requests, that is 1,000 bad events. A time-based equivalent is roughly 43.2 minutes in a 30-day month, but request-based measurement better reflects variable traffic.

Exclude only failures the service cannot reasonably control and document exclusions. Do not hide dependency failures if users experience them.

## Design questions

- Which journey matters: login, write, read, or end-to-end checkout?
- Does “good” include a latency threshold and correct response, not only HTTP status?
- Are synthetic probes representative of user experience?
- Is the window rolling or calendar-based, and who can change it?

## Interview prompt

**Why not use CPU as an SLI?** CPU is a saturation signal, useful for diagnosis and capacity, but not a direct user outcome. Pair it with an availability or latency SLI so the team does not optimize a proxy at users’ expense.
