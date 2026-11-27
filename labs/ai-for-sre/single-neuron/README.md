# Single artificial neuron — learning lab

This lab demonstrates how a single artificial neuron calculates a weighted sum and applies an activation function.

## Learning objectives

- Calculate a weighted sum from inputs, weights and a bias.
- Apply the ReLU activation function.
- Observe how changing one weight changes the output.
- Distinguish manually changing a parameter from training a model.

## Requirements

- Python 3.10 or later.
- No third-party packages are required.

## Run the example

From this directory:

```bash
python neuron.py
```

Expected output:

```text
Original weighted sum / ReLU output: 0.690
Adjusted weighted sum / ReLU output: 0.405
Note: changing these weights manually is not model training.
```

## Run the tests

```bash
python -m unittest -v test_neuron.py
```

The tests validate the two worked weighted sums, the ReLU behavior, input validation and the neuron forward pass.

## Important distinction

This is a **forward-pass demonstration only**. The weights are hard-coded to make the arithmetic visible. There is no loss function, backpropagation, optimizer or training loop in this lab. Do not describe this script as a trained incident prediction model.

## SRE context

The input values are synthetic, normalized signals representing CPU utilization, memory utilization and error rate. They are not calibrated production features and the output is not an incident probability.
