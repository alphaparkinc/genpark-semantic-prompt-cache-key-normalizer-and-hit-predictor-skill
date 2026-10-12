"""Example usage for Semantic Prompt Cache Key Normalizer & Hit Predictor."""
from client import SemanticCacheKeyNormalizer

if __name__ == "__main__":
    raw = "Request ID 550e8400-e29b-41d4-a716-446655440000 at 2026-10-12T17:00:00Z: Summarize quarterly financial filings and risk factors."
    res = SemanticCacheKeyNormalizer.normalize_prompt_for_cache(raw)
    print("Canonical:", res["canonical_prompt"])
