# AI Engineering Learning Progress

Last reviewed: 2026-11-27

This tracker records only evidence visible in completed learning sessions. "Introduced" is not the same as "practiced" or "mastered". Do not infer completion from reading a chapter.

## Phase 1 — AI Fundamentals

| Topic | Status | Evidence so far | Knowledge gap / next action |
| --- | --- | --- | --- |
| AI vs ML vs deep learning | In progress | Introductory explanation provided | Complete a formal quiz and explain examples independently |
| Traditional rules vs ML | In progress | Compared rule-based thresholding with learning patterns | Build a synthetic example and identify trade-offs |
| Training vs inference | In progress | Concepts introduced and discussed | Explain offline training vs online inference in an architecture |
| Artificial neurons, weights and bias | In progress | Worked a single-neuron weighted-sum example | Run and modify the Python implementation |
| Forward propagation | In progress | Formula and example calculated | Implement and explain the result |
| Loss functions | In progress | Concept introduced | Compare a prediction with a target using a simple loss |
| Backpropagation | In progress | Discussed gradient calculation and chain rule | Explain gradient computation without conflating it with optimizer updates |
| Gradient descent | In progress | Explained parameter update; distinction from backpropagation corrected | Work through a small numeric gradient update |
| Overfitting and generalization | In progress | Concept introduced | Interpret training versus validation results |
| Data drift and concept drift | In progress | Distinguished input distribution changes from changed input-target relationship | Describe monitoring signals and a response plan |
| Transformers and RNNs | In progress | Conceptual comparison discussed | Draw and explain sequence-processing flow |
| Self-attention and Q/K/V | In progress | Attention formula and SRE retrieval analogy introduced | Explain what Q/K/V mean as learned projections |
| Multi-head attention | In progress | Concept introduced | Explain why independent learned projections can be useful |
| Positional information | In progress | Concept introduced | Compare learned positional embeddings and RoPE at a high level |
| Causal masking and generation | In progress | Autoregressive generation introduced | Explain why future tokens must be masked |

## Assessment record

| Date | Assessment | Result | Notes |
| --- | --- | --- | --- |
| 2026-11-27 | Neural network written explanations | Provisional 3.2/4 conceptual score | Strong explanation of weights and drift; needed correction distinguishing backpropagation (gradient calculation) from gradient descent (parameter update). This is not a formal quiz result. |
| 2026-11-27 | Single-neuron numeric check | Partial | Correct initial sum 0.69. For CPU weight 0.20, correct weighted sum is 0.405 (not 0.285); correction discussed. |
| — | Lesson 1 multiple-choice quiz | Not submitted | Pending |
| — | Lesson 2 multiple-choice quiz | Not submitted | Pending |
| — | Lesson 3 multiple-choice quiz | Not submitted | Pending |

## Practical exercise evidence

| Exercise | Status | Evidence |
| --- | --- | --- |
| Python single-neuron implementation | Not completed | Code provided; execution not reported |
| Transformer architecture diagram and explanation | Not completed | Assignment issued; response pending |

## Learning status definitions

- **Not started:** the topic has not been introduced.
- **In progress:** lesson material has been discussed or read; assessment/practice evidence is incomplete.
- **Practiced:** the learner completed an exercise and can explain the result.
- **Mastered:** the learner can independently explain, implement and pass a practical assessment.

## Next actions

1. Complete the Python neuron exercise and verify outputs 0.69 and 0.405.
2. Complete outstanding Phase 1 quizzes or targeted oral assessments.
3. Complete the transformer diagram/explanation assignment.
4. Continue with tokens, tokenization and embeddings after the current fundamentals are assessed.
