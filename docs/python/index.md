# Python automation

Use Python for small, testable operational tools—not opaque production control planes. Prefer standard library parsing, explicit timeouts, structured logs, and dry-run mode.

```python
from urllib.request import urlopen

def healthy(url: str) -> bool:
    with urlopen(url, timeout=3) as response:  # no retry loop hidden here
        return 200 <= response.status < 300
```

Validate user input, avoid shell interpolation, authenticate with short-lived credentials, and make writes idempotent. A tool that changes state should require an explicit target and confirmation, log an audit record, and return non-zero on failure.

**Interview question:** How would you productionize a script? Define its contract and failure modes, add unit tests and static checks, package dependencies, use structured logging/metrics, constrain identity, document rollback, and decide whether a controller or existing platform is the safer owner.
