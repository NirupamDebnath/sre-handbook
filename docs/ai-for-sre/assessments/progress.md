# AI Engineering Learning Progress

Last reviewed: 2026-11-27

This tracker records lesson understanding, assessment attempts and GitHub solution artifacts separately. An answer key or mentor-authored solution is useful study material, but is not evidence that the learner independently passed an assessment.

## Phase 1 — AI Fundamentals

| Topic | Status | Evidence so far | Knowledge gap / next action |
| --- | --- | --- | --- |
| AI vs ML vs deep learning | In progress | Introductory explanation and reference answer key documented | Complete a fresh quiz and explain examples independently |
| Traditional rules vs ML | In progress | Compared rule-based thresholding with learning patterns | Build a synthetic example and identify trade-offs |
| Training vs inference | In progress | Concepts introduced and discussed | Explain offline training vs online inference in an architecture |
| Artificial neurons, weights and bias | In progress | Worked single-neuron calculation; runnable implementation committed | Run/modify the lab and explain the forward pass |
| Forward propagation | In progress | Formula and two numeric outputs verified by unit tests | Explain the implementation without relying on the code comments |
| Loss functions | In progress | Concept introduced; reference answer documented | Compare prediction and target using a small numeric example |
| Backpropagation | In progress | Discussed gradient calculation and chain rule | Explain gradient computation independently |
| Gradient descent | In progress | Difference from backpropagation corrected | Work through a numeric gradient update |
| Overfitting and generalization | In progress | Concept introduced | Interpret training versus validation results |
| Data drift and concept drift | In progress | Distinguished input distribution changes from changed input-target relationship | Describe monitoring signals and a response plan |
| Transformers and RNNs | In progress | Conceptual comparison and reference flow documented | Explain sequence processing independently |
| Self-attention and Q/K/V | In progress | Attention formula and SRE analogy introduced; answer key documented | Explain Q/K/V as learned projections |
| Multi-head attention | In progress | Concept introduced | Explain why independent learned projections can be useful |
| Positional information | In progress | Concept introduced | Compare learned positional embeddings and RoPE at a high level |
| Causal masking and generation | In progress | Autoregressive generation introduced; reference flow documented | Explain causal masking without the answer key |

## Assessment record

| Date | Assessment | Result | Notes |
| --- | --- | --- | --- |
| 2026-11-27 | Neural network written explanations | Provisional 3.2/4 conceptual score | Strong explanation of weights and drift; needed correction distinguishing backpropagation (gradient calculation) from gradient descent (parameter update). This is not a formal quiz result. |
| 2026-11-27 | Single-neuron numeric check | Arithmetic corrected and verified | Original weighted sum 0.690; after changing CPU weight to 0.20, the correct weighted sum is 0.405 (not 0.285). |
| — | Lesson 1 multiple-choice quiz | Answer key committed; learner attempt not submitted | No quiz score recorded |
| — | Lesson 2 multiple-choice quiz | Answer key committed; learner attempt not submitted | No quiz score recorded |
| — | Lesson 3 multiple-choice quiz | Answer key committed; learner attempt not submitted | No quiz score recorded |

## Hands-on artifact record

| Exercise | Artifact status | Evidence | Learner evidence / mastery |
| --- | --- | --- | --- |
| AI incident assistant design | Solution committed | `docs/ai-for-sre/labs/incident-assistant-design.md` includes architecture, inputs, output contract, investigation flow, safety and acceptance criteria | Reference solution is available; no independent learner submission recorded |
| Single-neuron Python implementation | Solution committed; 7 tests pass locally | `labs/ai-for-sre/single-neuron/neuron.py`, `test_neuron.py`, and README include implementation, tests and run instructions | Arithmetic discussed; learner execution/independent modification not yet reported |
| Transformer architecture flow | Solution committed | `docs/ai-for-sre/labs/transformer-flow.md` includes Mermaid flow and explanation | Reference solution is available; independent learner explanation not assessed |

The single-neuron tests were run locally using Python's standard-library `unittest` and all seven passed. GitHub Actions is configured to run these tests together with the strict MkDocs build; the pull request/CI result will be recorded after validation.

## Hands-on artifact completion policy

A hands-on artifact is complete when the required implementation and/or documentation is committed to the repository and its relevant checks pass.

- Coding tasks normally require runnable source, tests, and a README with commands and expected output.
- Design/reasoning tasks normally require a Markdown solution with diagrams, assumptions, trade-offs, safety and acceptance criteria.
- Mixed tasks require both code and documentation when both are necessary for reproducibility and review.
- Prefer a branch and pull request, then merge to `main` after review and CI. A branch-only solution is committed/in review, not merged.
- Artifact completion is tracked separately from learner mastery. A committed reference solution does not prove the learner can independently explain or implement it.

## Learning status definitions

- **Not started:** the topic has not been introduced.
- **In progress:** lesson material has been discussed or read; assessment/practice evidence is incomplete.
- **Practiced:** the learner completed an exercise and can explain the result.
- **Mastered:** the learner can independently explain, implement and pass a practical assessment.

## Next actions

1. Review the answer keys for Lessons 1–3, then take fresh quizzes without referring to the key.
2. Run the single-neuron lab locally and modify the input/weights; explain the results.
3. Explain the incident-assistant and transformer-flow designs in your own words.
4. Continue with tokens, tokenization and embeddings after the current fundamentals are assessed.
