"""Semantic Prompt Cache Key Normalizer & Hit Predictor.
100% Python Standard Library.
"""

import re

class SemanticCacheKeyNormalizer:
    """Normalizes whitespace, volatile timestamps, and request UUIDs in prompts to maximize deterministic prefix cache hits."""

    @staticmethod
    def normalize_prompt_for_cache(prompt: str) -> dict:
        scrubbed = re.sub(r"\b[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\b", "<UUID>", prompt)
        scrubbed = re.sub(r"\b20\d{2}-\d{2}-\d{2}[T ]\d{2}:\d{2}:\d{2}(?:\.\d+)?Z?\b", "<ISO_TIMESTAMP>", scrubbed)
        scrubbed = re.sub(r"\s+", " ", scrubbed).strip()

        volatile_removed = (scrubbed != re.sub(r"\s+", " ", prompt).strip())
        return {
            "canonical_prompt": scrubbed,
            "volatile_tokens_scrubbed": volatile_removed,
            "cache_eligibility": "HIGH" if len(scrubbed) >= 64 else "LOW_SHORT_PROMPT"
        }
