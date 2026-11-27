# Lab: A single artificial neuron

**Status:** Solution committed; reproducible unit tests included.

This is the first runnable Python lab in the AI fundamentals path. It demonstrates a forward pass using synthetic, normalized SRE signals.

## Source code

- [Python implementation](https://github.com/NirupamDebnath/sre-handbook/blob/main/labs/ai-for-sre/single-neuron/neuron.py)
- [Unit tests](https://github.com/NirupamDebnath/sre-handbook/blob/main/labs/ai-for-sre/single-neuron/test_neuron.py)
- [Lab README and run instructions](https://github.com/NirupamDebnath/sre-handbook/blob/main/labs/ai-for-sre/single-neuron/README.md)

## Run locally

```bash
cd labs/ai-for-sre/single-neuron
python neuron.py
python -m unittest -v test_neuron.py
```

No third-party Python package is needed.

## Worked result

Inputs are `[0.95, 0.85, 0.20]` and bias is `-0.20`.

| Configuration | Weights | Weighted sum |
| --- | --- | ---: |
| Original | `[0.50, 0.30, 0.80]` | 0.690 |
| CPU weight changed manually | `[0.20, 0.30, 0.80]` | 0.405 |

Both values are positive, so ReLU returns the same values.

## What this lab does not do

The example does not train a neural network. It has no loss calculation, backpropagation, optimizer or automatic parameter updates. The weights are manually supplied to isolate the forward-pass calculation.

## Completion evidence

The solution is committed as Python source with standard-library unit tests and reproducible instructions. CI runs the tests. This satisfies the repository-artifact completion criterion; it does not by itself establish independent learner mastery.
