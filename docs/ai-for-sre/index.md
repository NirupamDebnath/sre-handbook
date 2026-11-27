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

[Open the Lesson 1–3 knowledge-check answer keys](assessments/answer-keys.md).

## Hands-on solutions

- [AI incident assistant design](labs/incident-assistant-design.md) — reference architecture, evidence inputs, output contract, safety boundaries and acceptance criteria.
- [Single-neuron Python lab](labs/single-neuron.md) — runnable implementation, unit tests and instructions.
- [Transformer flow design](labs/transformer-flow.md) — documented decoder-only generation flow.

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

Each chapter includes learning objectives, prerequisites, first-principles explanations, diagrams, worked examples, SRE applications, limitations, a hands-on assignment, knowledge checks and references. Answer keys are maintained separately so the lesson pages can still be used for revision.

## Hands-on completion and evidence policy

A hands-on solution is considered **artifact-complete** when its necessary solution files are committed to this GitHub repository and the relevant validation passes. Use the format that fits the task:

- **Coding lab:** commit runnable source code, tests and a README with setup/run instructions and expected results. Add design documentation when it materially helps explain the implementation.
- **Architecture or reasoning lab:** commit a Markdown solution with diagrams (Mermaid where useful), assumptions, trade-offs, safety considerations and acceptance criteria. Code is not required unless implementation is part of the task.
- **Mixed lab:** commit both the implementation and the explanatory documentation/tests when both are needed for reproducibility and review.

For best practice, changes are submitted through a branch and pull request, reviewed, validated by CI and merged to `main`. A solution on a branch is recorded as committed/in review, not yet merged.

Artifact completion is not the same as learner mastery. The tracker separately records whether the learner ran, modified and explained the solution. Mastery still requires independent explanation, implementation and practical assessment.

## Learning status definitions

- **Not started:** no lesson work recorded.
- **In progress:** material has been introduced or studied.
- **Practiced:** the learner has completed an exercise and can explain the result.
- **Mastered:** the learner can independently explain, implement and pass a practical assessment.

A discussion, answer key or mentor-authored reference solution alone does not establish mastery.
