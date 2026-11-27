# Tokenization Inspection Lab

## Objective

Inspect how a model tokenizer converts synthetic SRE text into token IDs. Compare token counts across ordinary text, Kubernetes identifiers, JSON and a Bengali sentence.

## Prerequisites

- Python 3.9 or later.
- Basic command-line and Python knowledge.
- No model API key is required. The tokenizer runs locally after its package and encoding data are available.

## Run the lab

From the repository root:

~~~bash
python -m pip install -r labs/ai-for-sre/tokenization/requirements.txt

python labs/ai-for-sre/tokenization/tokenization.py \
  "payment-api returned HTTP 503 after deployment"
~~~

The demo uses the **o200k_base** encoding. Select the encoding associated with the model you plan to call when using this in a real application.

## Experiments

Run the program for each of these synthetic inputs:

1. Plain English: The payment service is returning HTTP 503 errors.
2. Kubernetes identifier: payment-api-7c9d8f6b5d-x2kqv OOMKilled
3. JSON: {"service":"payment-api","status":503,"retry":true}
4. Bengali: পেমেন্ট সার্ভিসে সমস্যা হচ্ছে

Record the input character count, approximate word count and actual token count. Do not assume a fixed relationship between these values.

## Questions to answer

- Which input produced the most tokens relative to its character count?
- Did the Kubernetes identifier or JSON tokenize like ordinary prose?
- Why is the actual tokenizer result more useful than a word-count estimate?
- How could you reduce noisy log input while retaining timestamps, service identity, error class and causal evidence?

## Acceptance criteria

- The script runs successfully and displays token IDs and token-byte pieces.
- All unit tests pass.
- You submit a short Markdown note with your four observations and one proposed log-preprocessing strategy.
- Your note uses synthetic data only.

## Implementation

- [Python source](https://github.com/NirupamDebnath/sre-handbook/blob/main/labs/ai-for-sre/tokenization/tokenization.py)
- [Unit tests](https://github.com/NirupamDebnath/sre-handbook/blob/main/labs/ai-for-sre/tokenization/test_tokenization.py)
- [Lab README](https://github.com/NirupamDebnath/sre-handbook/blob/main/labs/ai-for-sre/tokenization/README.md)

## Safety note

Do not use production logs, customer data, internal hostnames, credentials, secrets or proprietary code. Build and test with synthetic incident examples in a personal lab.
