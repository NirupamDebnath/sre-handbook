# Networking and request-path debugging

Debug from name resolution through TLS, routing, load balancer, and application response. A connection failure does not identify its layer by itself.

```bash
dig +short api.example.test       # Resolver answer; compare expected record/TTL
curl -sv --connect-timeout 3 https://api.example.test/health
ss -s                             # Socket summary; look for pressure trends
```

`curl -v` shows DNS, TCP, TLS, and HTTP timing boundaries but can print headers; redact tokens. `tcpdump` is powerful but captures traffic contents: use narrow filters, a short duration, least privilege, and approved handling.

## Failure patterns

- **DNS:** compare resolver, search domain, record type, TTL, and negative-cache behavior.
- **TLS:** check hostname/SNI, certificate chain, clock, supported protocol/cipher, and proxy termination point.
- **Exhaustion:** inspect ephemeral-port use, TIME_WAIT, connection pooling, file descriptors, and downstream latency.
- **Latency:** decompose client, DNS, connect, TLS, time-to-first-byte, and response phases before changing timeouts.

## Interview question

**Retries made an outage worse—why?** Retries multiply offered load when a dependency is saturated. Use a bounded retry budget, exponential backoff with jitter, idempotency keys for writes, circuit breaking, and load shedding. Measure retry volume separately.
