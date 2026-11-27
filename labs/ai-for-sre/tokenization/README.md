# Tokenization inspection lab

This lab uses OpenAI's open-source **tiktoken** package to inspect token IDs and token-byte pieces. It does not call a model API and does not require an API key.

## Requirements

- Python 3.9 or later.
- Internet access may be required on the first run to install the package and retrieve tokenizer data.
- Use synthetic text only.

## Setup

From the repository root:

~~~bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r labs/ai-for-sre/tokenization/requirements.txt
~~~

On Windows PowerShell, activate the environment with:

~~~powershell
.venv\Scripts\Activate.ps1
~~~

## Run

~~~bash
python labs/ai-for-sre/tokenization/tokenization.py \
  "payment-api returned HTTP 503 after deployment"
~~~

Choose a different encoding with the **--encoding** option:

~~~bash
python labs/ai-for-sre/tokenization/tokenization.py \
  --encoding o200k_base \
  "payment-api-7c9d8f6b5d-x2kqv OOMKilled"
~~~

The default **o200k_base** encoding is a demonstration. For production token budgeting, select the encoding used by the exact model being called. Check the tokenizer/model mapping in the current library documentation.

## Tests

The unit tests use a deterministic fake byte encoder, so they do not need to download tokenizer vocabulary data:

~~~bash
python -m unittest discover \
  -s labs/ai-for-sre/tokenization \
  -p 'test_*.py' \
  -v
~~~

## Expected output

The exact IDs and count depend on the input and selected encoding. The script prints:

- Original text and character count.
- Total token count.
- Each token ID and its byte representation.
- A round-trip check confirming that concatenated token bytes reconstruct the original text.

A token can contain only part of a multi-byte UTF-8 character. For that reason, the script prints byte representations instead of decoding every token as an independent Unicode string.

## Implementation notes

- The **inspect_text** function accepts a small protocol, making it easy to unit test without importing **tiktoken**.
- The external dependency is imported only by the CLI entry point.
- The code checks that the complete byte sequence round-trips to the original text.
- The fake encoder tests validate the inspection wrapper, not the internal correctness of BPE or the external package.

## Safety

Never use internal production logs, customer data, credentials, secrets, internal hostnames or proprietary source code. Use synthetic examples in a personal lab.
