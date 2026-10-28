# AI for SRE

Useful AI-assisted operations are bounded systems, not autonomous root-cause machines. Good starter projects summarize an approved incident channel, retrieve versioned runbooks, correlate alert metadata, or draft a handoff—while a human remains accountable for decisions and state changes.

## A practical roadmap

1. Choose a low-risk read-only use case and define success: factual citation rate, time saved, and unsafe-output rate.
2. Index approved, access-controlled runbooks with source/version citations; filter retrieval by caller authorization.
3. Require structured output: impact, evidence, unknowns, suggested next checks, and links.
4. Evaluate against anonymized historical cases; test hallucination, stale documents, prompt injection, and data leakage.
5. Keep actions behind explicit human approval, least-privilege tools, audit logs, rate limits, and a kill switch.

Never send sensitive logs or customer data to an unapproved model endpoint. Alert correlation can suggest clusters, but it must surface evidence and uncertainty rather than silently suppress alerts.
