"""Inspect token IDs and byte pieces using a compatible tiktoken encoding."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from typing import Protocol


class TokenEncoder(Protocol):
    """Minimal interface required by the inspection function."""

    def encode(self, text: str) -> list[int]:
        """Convert text to token IDs."""

    def decode_single_token_bytes(self, token: int) -> bytes:
        """Return the original byte sequence for one token ID."""


@dataclass(frozen=True)
class TokenizationReport:
    """Tokenization result without assuming each token is valid UTF-8 alone."""

    text: str
    token_ids: list[int]
    token_bytes: list[bytes]

    @property
    def token_count(self) -> int:
        return len(self.token_ids)


def inspect_text(text: str, encoder: TokenEncoder) -> TokenizationReport:
    """Encode text and preserve each token's original bytes.

    Token boundaries may split a multi-byte UTF-8 character. Keeping bytes
    intact avoids misleading per-token Unicode decoding.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    token_ids = encoder.encode(text)
    token_bytes = [encoder.decode_single_token_bytes(token) for token in token_ids]
    return TokenizationReport(
        text=text,
        token_ids=token_ids,
        token_bytes=token_bytes,
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Inspect token IDs for a text string using tiktoken."
    )
    parser.add_argument(
        "text",
        nargs="?",
        default="payment-api returned HTTP 503 after deployment",
        help="Text to tokenize. Use synthetic data only.",
    )
    parser.add_argument(
        "--encoding",
        default="o200k_base",
        help="tiktoken encoding name (default: o200k_base).",
    )
    args = parser.parse_args()

    try:
        import tiktoken
    except ImportError as exc:
        raise SystemExit(
            "tiktoken is not installed. Run: "
            "python -m pip install -r "
            "labs/ai-for-sre/tokenization/requirements.txt"
        ) from exc

    try:
        encoder = tiktoken.get_encoding(args.encoding)
    except ValueError as exc:
        raise SystemExit(f"Unknown tiktoken encoding: {args.encoding}") from exc

    report = inspect_text(args.text, encoder)
    print(f"Text: {report.text}")
    print(f"Characters: {len(report.text)}")
    print(f"Tokens: {report.token_count}")
    print("Token breakdown (byte representation is intentional):")

    if len(report.token_ids) != len(report.token_bytes):
        raise RuntimeError("Token IDs and token byte pieces have different lengths")

    for index, token_id in enumerate(report.token_ids):
        token_bytes = report.token_bytes[index]
        print(f"  {index:>3}: id={token_id:<8} bytes={token_bytes!r}")

    reconstructed = b"".join(report.token_bytes).decode("utf-8")
    if reconstructed != report.text:
        raise RuntimeError("Decoded token bytes did not reconstruct the input")

    print("Round-trip check: passed")


if __name__ == "__main__":
    main()
