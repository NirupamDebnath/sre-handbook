"""A minimal, manually configured artificial neuron for learning.

This module demonstrates a forward pass only. It does not train a model.
All inputs and weights in the example are illustrative normalized values.
"""
from collections.abc import Callable, Sequence


def weighted_sum(
    inputs: Sequence[float],
    weights: Sequence[float],
    bias: float,
) -> float:
    """Calculate sum(input_i * weight_i) + bias."""
    if len(inputs) != len(weights):
        raise ValueError("inputs and weights must have equal lengths")

    return sum(value * weight for value, weight in zip(inputs, weights)) + bias


def relu(value: float) -> float:
    """Apply the ReLU activation function."""
    return max(0.0, value)


def neuron(
    inputs: Sequence[float],
    weights: Sequence[float],
    bias: float,
    activation: Callable[[float], float] = relu,
) -> float:
    """Run one forward pass through a single artificial neuron."""
    return activation(weighted_sum(inputs, weights, bias))


def main() -> None:
    features = [0.95, 0.85, 0.20]
    bias = -0.20

    original_weights = [0.50, 0.30, 0.80]
    adjusted_weights = [0.20, 0.30, 0.80]

    original_output = neuron(features, original_weights, bias)
    adjusted_output = neuron(features, adjusted_weights, bias)

    print(f"Original weighted sum / ReLU output: {original_output:.3f}")
    print(f"Adjusted weighted sum / ReLU output: {adjusted_output:.3f}")
    print("Note: changing these weights manually is not model training.")


if __name__ == "__main__":
    main()
