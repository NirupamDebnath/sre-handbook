# Tokens and Tokenization

## Learning objectives

- Define a token and distinguish it from a word, character, byte and token ID.
- Explain why language models require tokenization.
- Describe the intuition behind subword tokenization and Byte Pair Encoding (BPE).
- Explain why token counts matter for context capacity, latency and API cost.
- Inspect token IDs using Python and the tokenizer appropriate to a target model.

## 1. What is a token?

A **token** is a unit of text recognized by a language model's tokenizer. Depending on the tokenizer and text, a token may represent a whole word, part of a word, punctuation, whitespace or a sequence of bytes.

For example, a tokenizer might split:

- **incident** into one token.
- **tokenization** into multiple subword tokens.
- **payment-api** into several pieces, potentially including the hyphen.
- **OOMKilled** into one or more pieces.

These are illustrative possibilities, not guaranteed splits. The exact result depends on the tokenizer vocabulary and merge rules.

A token is not necessarily a word. Tokens, characters, bytes and words are different units:

| Unit | Example / meaning |
| --- | --- |
| Character | A Unicode text character such as A or é |
| Byte | An 8-bit unit used to encode text; one character may take multiple UTF-8 bytes |
| Word | A linguistic unit, often separated by spaces in English |
| Token | A unit defined by a model's tokenizer |
| Token ID | An integer identifying a token in the tokenizer vocabulary |

A rough English-language rule of thumb is around four characters per token, but it is not exact and should not be used for production budgeting. Token counts vary with language, punctuation, code, identifiers and the tokenizer. See the [OpenAI tokenizer](https://platform.openai.com/tokenizer) for an interactive demonstration.

## 2. Why tokenization is necessary

Neural networks operate on numerical inputs, not raw strings. A tokenizer converts input text into a sequence of token IDs from a vocabulary.

~~~mermaid
flowchart TD
    A[Input text] --> B[Tokenizer]
    B --> C[Token pieces]
    C --> D[Token IDs]
    D --> E[Embedding lookup]
    E --> F[Vectors consumed by transformer]
~~~

The token IDs are discrete identifiers. They are not yet semantic vectors. The model uses an embedding table to map each ID to a learned vector; embeddings are covered in Lesson 5.

## 3. Subword tokenization

A useful compromise between word-based and character-based approaches is **subword tokenization**.

- A word-based tokenizer can require an enormous vocabulary and struggles with unseen words.
- A character-based tokenizer can represent almost any text, but a word may require many small units and longer sequences.
- A subword tokenizer represents frequent sequences as larger units and can compose rarer words from smaller pieces.

One common approach is Byte Pair Encoding (BPE). Conceptually:

1. Begin with smaller units derived from the text.
2. Count adjacent pairs in a training corpus.
3. Merge frequent pairs into larger units.
4. Repeat until the vocabulary is built.
5. At inference time, use the learned vocabulary and merge priorities to encode text as token IDs.

This balances vocabulary size and the ability to represent unfamiliar words. Production implementations include pre-tokenization rules and byte-level details; the simplified steps above describe the intuition, not every implementation detail.

OpenAI's **tiktoken** is a fast BPE tokenizer used with OpenAI models. The Hugging Face course explains word-, character- and subword-based approaches and compares tokenizer algorithms.

## 4. Why tokens matter in production LLM systems

Imagine an AI incident assistant receives:

- 30 alert descriptions.
- 500 lines of synthetic application logs.
- 20 Kubernetes events.
- 5 deployment records.
- Relevant runbook excerpts.
- Conversation history.

All these items contribute to the model input. The generated response also consumes output tokens.

| Concern | SRE impact |
| --- | --- |
| Context capacity | Input and generated output must fit the model's supported context window. |
| Latency | Processing more tokens can increase response time. |
| Cost | Many model APIs meter usage by tokens; exact rates and categories depend on the provider and model. |
| Retrieval quality | Adding irrelevant documents consumes context without necessarily improving the answer. |

A production AI-SRE pipeline should filter noisy logs, deduplicate repeated alerts, retrieve relevant runbook sections and cap unnecessary history. It should not send every log line merely because it is available.

**Use the tokenizer for the target model when estimating token counts.** Different models may use different tokenizers. A count from another tokenizer is only an approximation.

## 5. Token ID versus embedding

These concepts are related but not interchangeable:

| Concept | Meaning |
| --- | --- |
| Token | A piece of text recognized by the tokenizer |
| Token ID | An integer identifying that token in a vocabulary |
| Embedding | A learned vector representation associated with a token ID or another item |

Think of the token ID as a dictionary entry number. The embedding is the numerical vector retrieved for that entry. Lesson 5 explains how these vectors represent learned relationships and how they support semantic search and retrieval.

## 6. Python inspection with tiktoken

The hands-on lab in **labs/ai-for-sre/tokenization/** uses **tiktoken** to show token IDs and the underlying bytes for each token.

~~~bash
python -m pip install -r labs/ai-for-sre/tokenization/requirements.txt
python labs/ai-for-sre/tokenization/tokenization.py "payment-api returned HTTP 503"
~~~

The example uses the **o200k_base** encoding as a demonstration. In an application, use the encoding associated with the exact model you call. Refer to the tokenizer library documentation for the current model-to-encoding mapping.

Token pieces are displayed as bytes because a token boundary does not always coincide with a Unicode character boundary. Decoding each token independently as ordinary text can produce replacement characters; the original sequence is reconstructed by concatenating the token bytes.

## 7. Limitations and trade-offs

- Token boundaries are model/tokenizer-specific; never hardcode illustrative token splits.
- Word-count and character-count estimates are not reliable substitutes for token counting.
- Some languages and unusual text can have different token-to-character ratios from common English.
- Logs, JSON, stack traces, IDs and code can tokenize differently from ordinary prose.
- Context budgeting must leave room for generated output and any system/tool instructions.
- Tokenization alone does not understand meaning. Semantic vector representations are a separate concept.

## Knowledge check

1. Why does a model need tokenization before processing text?
2. How is a token different from a word, a byte and a token ID?
3. Why is subword tokenization a compromise between word-based and character-based approaches?
4. Why should an AI incident assistant count tokens instead of estimating from the number of log lines?
5. Why can a tokenizer for one model produce a different count from another model's tokenizer?
6. What is the difference between a token ID and an embedding?

## Hands-on assignment

Complete the [Tokenization Inspection Lab](../labs/tokenization.md):

1. Run the script on a short synthetic incident message.
2. Run it on a longer synthetic log excerpt.
3. Compare ordinary English, a Kubernetes identifier, JSON and a Bengali sentence.
4. Record the token count for each input and explain why character or word counts alone do not predict the result.
5. Propose one safe preprocessing strategy to reduce prompt size without discarding incident evidence.

Use only synthetic data. Do not paste employer logs, production identifiers, customer information, credentials or proprietary code into public or unapproved tools.

## Further learning resources

| Resource | Creator | Recommended use |
| --- | --- | --- |
| [OpenAI Tokenizer](https://platform.openai.com/tokenizer) | OpenAI | Interactive tokenizer; compare text and token counts |
| [tiktoken README](https://github.com/openai/tiktoken) | OpenAI | Python tokenizer installation, encodings and BPE details |
| [Tokenizers course chapter](https://huggingface.co/docs/course/chapter2/4) | Hugging Face | Read the explanation of word, character and subword tokenization |
| [Tokenizers Overview video](https://www.youtube.com/watch?v=VFp38yj8h3A) | Hugging Face | Watch for a visual introduction to tokenization strategies |

Suggested order: use the OpenAI tokenizer first, read the Hugging Face chapter, then run the local Python lab. Watching a video is useful context but does not replace the lab or knowledge check.

## References

- [OpenAI tokenizer](https://platform.openai.com/tokenizer)
- [OpenAI tiktoken repository](https://github.com/openai/tiktoken)
- [Hugging Face Course: Tokenizers](https://huggingface.co/docs/course/chapter2/4)
- [OpenAI Cookbook: Counting tokens with tiktoken](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_count_tokens_with_tiktoken.ipynb)

## Progress

**Status: In progress.** Tokenization and token IDs have been introduced and a runnable inspection lab is provided. The learner's knowledge check and hands-on evidence remain to be submitted.
