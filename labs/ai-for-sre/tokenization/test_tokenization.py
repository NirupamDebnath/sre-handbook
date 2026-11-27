"""Unit tests for the tokenizer inspection logic (no external package needed)."""

from __future__ import annotations

import unittest

from tokenization import inspect_text


class FakeByteEncoder:
    """A deterministic byte-level fake for testing the inspection wrapper."""

    def encode(self, text: str) -> list[int]:
        return list(text.encode("utf-8"))

    def decode_single_token_bytes(self, token: int) -> bytes:
        return bytes([token])


class TokenizationInspectionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.encoder = FakeByteEncoder()

    def test_ascii_text_token_count(self) -> None:
        report = inspect_text("abc", self.encoder)
        self.assertEqual(report.token_count, 3)
        self.assertEqual(report.token_ids, [97, 98, 99])

    def test_empty_text_has_no_tokens(self) -> None:
        report = inspect_text("", self.encoder)
        self.assertEqual(report.token_count, 0)
        self.assertEqual(report.token_ids, [])
        self.assertEqual(report.token_bytes, [])

    def test_unicode_bytes_are_preserved(self) -> None:
        text = "é"
        report = inspect_text(text, self.encoder)
        self.assertEqual(b"".join(report.token_bytes), text.encode("utf-8"))
        self.assertEqual(report.token_count, 2)

    def test_token_bytes_match_token_ids(self) -> None:
        report = inspect_text("503", self.encoder)
        self.assertEqual(len(report.token_ids), len(report.token_bytes))
        self.assertEqual(b"".join(report.token_bytes), b"503")

    def test_non_string_input_is_rejected(self) -> None:
        with self.assertRaises(TypeError):
            inspect_text(503, self.encoder)  # type: ignore[arg-type]


if __name__ == "__main__":
    unittest.main()
