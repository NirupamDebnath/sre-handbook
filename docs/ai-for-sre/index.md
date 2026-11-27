# AI for SRE

AI for Site Reliability Engineering combines machine learning, large language models, retrieval, and carefully governed automation to improve operational understanding and reduce toil.

The objective is not to replace engineering judgement with an autonomous root-cause machine. A production-grade AI-SRE system should expose evidence, uncertainty, provenance, authorization boundaries, and safe next steps.

## Learning path

| Phase | Focus | Status |
| --- | --- | --- |
| 1. AI fundamentals | AI, ML, deep learning, neural networks, transformers, tokens, embeddings, training and inference | In progress |
| 2. Python for AI | APIs, async Python, validation, structured outputs, errors and tests | Not started |
| 3. LLM applications | Prompt design, retrieval, vector search, RAG and evaluation | Not started |
| 4. AI agents | Tool calling, orchestration, permissions, memory and approval | Not started |
| 5. AI for SRE | Incident summarization, alert correlation, log analysis, RCA and runbook workflows | Not started |
| 6. LLMOps | Serving, gateways, observability, latency, cost, security and reliability | Not started |
| 7. AI infrastructure | GPUs, quantization, inference optimization and Kubernetes model serving | Not started |

## AI fundamentals — chapters

1. [AI, machine learning and deep learning](fundamentals/ai-ml-deep-learning.md)
2. [Neural networks and model training](fundamentals/neural-networks.md)
3. [Transformers and attention](fundamentals/transformers-attention.md)
4. Tokens and tokenization — planned
5. Embeddings — planned

## Practical project roadmap

Build progressively with synthetic data and a personal lab:

1. AI incident summarizer using alerts, logs and deployment events.
2. Kubernetes troubleshooting assistant grounded in documentation and runbooks.
3. RAG-based SRE knowledge assistant.
4. Read-only incident investigation agent with explicit permission boundaries.
5. AI observability platform measuring latency, errors, token use and answer quality.
6. End-to-end production AI-SRE platform.

## Operating principles

- Use synthetic or explicitly approved data. Never place employer-confidential logs, customer data, credentials, secrets or proprietary code into an unapproved model or lab.
- Start with read-only workflows. Keep production changes behind explicit human approval.
- Require evidence and source references for operational claims.
- Treat model output as a hypothesis, not ground truth.
- Evaluate quality, safety, latency, reliability and cost before deployment.
- Apply least privilege, authorization-aware retrieval, audit logging, rate limits and a kill switch.

## Chapter conventions

Each chapter includes learning objectives, prerequisites, first-principles explanations, diagrams, worked examples, SRE applications, limitations, a hands-on assignment, knowledge checks and references.

Progress labels are evidence-based:

- **Not started:** no lesson work recorded.
- **In progress:** material has been introduced or studied.
- **Practiced:** the learner completed an exercise and can explain the result.
- **Mastered:** the learner can independently explain, implement and pass a practical assessment.

A discussion or video alone does not establish mastery.
