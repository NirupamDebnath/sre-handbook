"""Unit tests for the single-neuron learning example."""
import unittest

from neuron import neuron, relu, weighted_sum


class WeightedSumTests(unittest.TestCase):
    def test_original_weighted_sum_is_069(self) -> None:
        result = weighted_sum(
            inputs=[0.95, 0.85, 0.20],
            weights=[0.50, 0.30, 0.80],
            bias=-0.20,
        )
        self.assertAlmostEqual(result, 0.69)

    def test_adjusted_cpu_weight_produces_0405(self) -> None:
        result = weighted_sum(
            inputs=[0.95, 0.85, 0.20],
            weights=[0.20, 0.30, 0.80],
            bias=-0.20,
        )
        self.assertAlmostEqual(result, 0.405)

    def test_input_and_weight_lengths_must_match(self) -> None:
        with self.assertRaises(ValueError):
            weighted_sum(inputs=[0.95, 0.85], weights=[0.50], bias=-0.20)


class ActivationAndNeuronTests(unittest.TestCase):
    def test_relu_returns_zero_for_negative_values(self) -> None:
        self.assertEqual(relu(-1.5), 0.0)

    def test_relu_preserves_positive_values(self) -> None:
        self.assertEqual(relu(0.69), 0.69)

    def test_neuron_applies_relu_to_weighted_sum(self) -> None:
        result = neuron(
            inputs=[0.95, 0.85, 0.20],
            weights=[0.50, 0.30, 0.80],
            bias=-0.20,
        )
        self.assertAlmostEqual(result, 0.69)

    def test_neuron_returns_zero_for_negative_weighted_sum(self) -> None:
        result = neuron(inputs=[1.0], weights=[-2.0], bias=0.0)
        self.assertEqual(result, 0.0)


if __name__ == "__main__":
    unittest.main()
