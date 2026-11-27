# AI Fundamentals — Knowledge Check Answer Key

> **Purpose:** Instructor/reference answers for the knowledge checks included in Lessons 1–3. These are explanations, not evidence that the learner submitted or passed the corresponding quizzes. The progress tracker records assessment attempts separately.

## Lesson 1 — AI, machine learning and deep learning

### Multiple-choice answer key

| Question | Answer | Explanation |
| --- | --- | --- |
| 1. What best describes traditional programming? | **B — A developer explicitly defines rules and logic.** | The program follows logic specified by its developers rather than learning the decision rule from examples. |
| 2. What is the main difference between ML and traditional rule-based programming? | **B — ML learns patterns from data rather than relying only on explicitly written rules.** | ML algorithms fit model parameters from data. Developers still choose the data, objective, model and training procedure. |
| 3. What is inference? | **C — Using a trained model to produce a prediction or response.** | Inference is model use after or during training, not the parameter-fitting process itself. |
| 4. An LLM belongs primarily to which category? | **B — Deep learning.** | Modern general-purpose LLMs are deep neural networks, typically based on transformer architectures. |
| 5. Can an assistant with no cluster API access independently verify current cluster state? | **B — No; it needs relevant supplied data or authorized tools.** | A model cannot inspect external systems merely because it knows Kubernetes concepts. The application must provide current information or controlled tools. |

### Written assignment — design an AI incident assistant

Scenario: \`payment-api\` on Kubernetes has an HTTP 500 error rate above 20%, three pod restarts, database connection timeouts and a deployment that completed 10 minutes before the symptoms.

**1. What information should the assistant receive?**

- Alert name, severity, labels, start time and affected service/namespace/cluster.
- Relevant time-bounded logs, with timestamps and trace/request correlation identifiers where available.
- Metrics such as request rate, error rate, latency, CPU, memory, restarts and database connection saturation/timeouts.
- Distributed traces and dependency spans, where available.
- Deployment and configuration-change events, Kubernetes events and pod/container state.
- Approved runbooks and service ownership/dependency metadata.

Normalize timestamps and identify the time window. Apply access controls and redact secrets or sensitive data before sending context to a model.

**2. What should it generate?**

A structured incident brief containing:

- Impact and scope.
- A chronological event timeline.
- Observed facts, each linked to its evidence source.
- Possible causes, with supporting and contradicting evidence.
- Unknowns and missing telemetry.
- Safe next investigative checks.
- A concise handoff summary.

It should label hypotheses as hypotheses, not present them as confirmed root cause.

**3. How can it identify a likely cause?**

Correlate the deployment timestamp with the beginning of the error increase. Compare pre- and post-deployment metrics; inspect changed configuration/image versions; examine database timeout logs and traces; correlate pod restarts with termination reasons, readiness failures and resource pressure. Compare multiple hypotheses and state what evidence would confirm or refute each. Temporal proximity is a clue, not proof that the deployment caused the incident.

**4. What must it not do independently?**

It must not restart/delete pods, roll back a deployment, scale workloads, change configuration, alter database settings, silence alerts or run other state-changing production commands without an explicit authorization and human approval workflow. Begin with least-privilege read-only tools.

**5. How should hallucinations be controlled?**

- Ground answers in supplied telemetry and approved, versioned runbooks.
- Require evidence references for operational claims.
- Separate observed facts from inferences and recommendations.
- Require the assistant to say when evidence is missing or contradictory.
- Use structured output and validate it.
- Test against synthetic incidents, including misleading or incomplete evidence.
- Evaluate factuality, citation correctness, unsafe recommendations and abstention behaviour.

This is a reference solution. The learner did not submit the original five-part assignment in the conversation.

---

## Lesson 2 — Neural networks and model training

### Multiple-choice answer key

| Question | Answer | Explanation |
| --- | --- | --- |
| 1. What does a weight represent? | **B — The influence of an input on the neuron's calculation.** | The weight scales that input's contribution to the weighted sum. |
| 2. What is the purpose of a loss function? | **B — Measure prediction error.** | The loss quantifies how the prediction differs from the training target under the selected objective. |
| 3. What does backpropagation calculate? | **B — Gradients of loss with respect to model parameters.** | It applies the chain rule through the computation graph. |
| 4. What can happen with an excessively high learning rate? | **C — Updates may overshoot and training may become unstable.** | Large parameter steps can jump across a minimum or cause loss to diverge. |
| 5. What describes a model that performs well on training data but poorly on unseen data? | **C — Overfitting.** | The model has fit patterns specific to training examples that do not generalize well. |

### Written concepts

**Why do neural networks need weights?**

Weights control how strongly each input contributes to a neuron's weighted sum. During training they are adjusted so that the network can fit relationships in the training data. The weights are parameters; they are not an explanation of causality.

**Backpropagation versus gradient descent**

Backpropagation calculates the gradients of the loss with respect to parameters by applying the chain rule. Gradient descent (or another optimizer) uses those gradients to update the parameters. Backpropagation computes gradient information; the optimizer performs the update.

For a simple gradient-descent update:

\`\`\`text
new_weight = old_weight - learning_rate * gradient
\`\`\`

**Why can high training accuracy fail in production?**

Training accuracy measures fit on training data, not necessarily generalization. The model may be overfit, the evaluation data may not represent production, features may be missing or incorrectly computed, or production data/target relationships may have changed. Compare training, validation and held-out test performance, then monitor production input distributions and outcome quality.

**Data drift versus concept drift**

- Data drift: the distribution of incoming features changes.
- Concept drift: the relationship between features and the target changes.

### Worked single-neuron calculation

Inputs: \`[0.95, 0.85, 0.20]\`; weights: \`[0.50, 0.30, 0.80]\`; bias: \`-0.20\`.

Original weighted sum:

\`\`\`text
(0.95 * 0.50) + (0.85 * 0.30) + (0.20 * 0.80) - 0.20
= 0.475 + 0.255 + 0.160 - 0.200
= 0.690
\`\`\`

After changing only the CPU weight from \`0.50\` to \`0.20\`:

\`\`\`text
(0.95 * 0.20) + (0.85 * 0.30) + (0.20 * 0.80) - 0.20
= 0.190 + 0.255 + 0.160 - 0.200
= 0.405
\`\`\`

With ReLU activation, both values remain unchanged because both are positive. The second result is **0.405**, not 0.285.

**Does manually changing a weight mean the model has learned?**

No. It changes a parameter but does not perform a learning procedure. Training uses examples, a loss function, backpropagated gradients and an optimizer to update parameters. The resulting model must still be evaluated on separate data to determine whether it generalizes.

### Hands-on implementation

The runnable implementation and unit tests are maintained in [\`labs/ai-for-sre/single-neuron/\`](https://github.com/NirupamDebnath/sre-handbook/tree/main/labs/ai-for-sre/single-neuron). The [lab guide](../labs/single-neuron.md) explains how to run them.

---

## Lesson 3 — Transformers and attention

### Multiple-choice answer key

| Question | Answer | Explanation |
| --- | --- | --- |
| 1. Why were transformers a major improvement over traditional RNNs? | **B — They use attention to relate tokens and allow more parallelism during training.** | RNNs have a sequential dependency across positions; transformer self-attention can process position representations together during training. |
| 2. What is the purpose of self-attention? | **B — Determine how much information tokens should receive from other tokens.** | It calculates attention weights and combines value representations to form contextual outputs. |
| 3. What does the Query vector represent? | **A — The information being searched for or matched against.** | A query is compared with keys to produce attention scores. |
| 4. Why do transformers need positional information? | **C — To provide information about token order.** | Attention alone does not inherently identify the original sequence order. |
| 5. Why does GPT use causal masking? | **A — To prevent access to future tokens during next-token prediction.** | A position must not use tokens that occur after it in the autoregressive prediction objective. |

### Written assignment — explain attention

**1. Why is attention useful for relationships between distant words?**

Self-attention lets a token's representation directly incorporate information from other positions in the available sequence. It avoids requiring information to pass through every intermediate recurrent step. The computation across positions can be parallelized during training, although standard full attention has a substantial sequence-length cost.

**2. Explain Q, K and V with a Kubernetes troubleshooting analogy.**

For an OOMKilled investigation, imagine a retrieval system looking for memory-pressure guidance:

- Query: the representation of what the current token/position is matching against.
- Key: the representation used to score how relevant another position is.
- Value: the information from that position that is weighted and combined.

In a troubleshooting analogy, a search request is matched against indexed runbook descriptors and the relevant runbook content is retrieved. This is only an analogy: transformer Q/K/V are learned vector projections inside the model, not actual runbook fields or a vector database lookup.

**3. Why can't a causal GPT model attend to future tokens?**

GPT-style autoregressive training predicts the next token from preceding context. A causal mask blocks attention to future positions so the model cannot leak the answer from tokens it is supposed to predict. At generation time those future tokens do not exist yet.

### Reference flow for the transformer diagram exercise

\`\`\`mermaid
flowchart TD
    P[Prompt text] --> T[Tokenization]
    T --> E[Token embeddings]
    E --> POS[Add positional information]
    POS --> DEC[Decoder transformer blocks]
    DEC --> ATT[Masked self-attention]
    ATT --> FFN[Feed-forward network]
    FFN --> LOGITS[Next-token scores]
    LOGITS --> SELECT[Decoding / token selection]
    SELECT --> APPEND[Append selected token]
    APPEND --> DEC
\`\`\`

For an AI incident assistant, the surrounding application separately retrieves authorized telemetry, deployment events and runbooks, then supplies relevant context to the model. The transformer flow by itself does not connect to Kubernetes, monitoring systems or a knowledge base.

This is a reference design committed as documentation. It does not record that the learner independently drew or explained the diagram.

---

## Assessment integrity

The answer keys are available for revision. The multiple-choice quizzes for Lessons 1–3 were presented in the learning sessions but were not submitted by the learner. Therefore, no quiz score or pass is recorded here. Review the explanations, then take a fresh assessment without using this key.
