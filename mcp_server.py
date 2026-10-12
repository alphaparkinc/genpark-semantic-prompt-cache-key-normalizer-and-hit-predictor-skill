"""MCP server for Semantic Prompt Cache Key Normalizer & Hit Predictor."""
import sys
import json
from client import SemanticCacheKeyNormalizer

def handle_request(req):
    method = req.get("method")
    if method == "tools/list":
        return {
            "tools": [{
                "name": "normalize_prompt_cache_key",
                "description": "Normalizes volatile UUIDs and timestamps in prompts to improve prefix cache hit rates",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "prompt": {"type": "string"}
                    },
                    "required": ["prompt"]
                }
            }]
        }
    elif method == "tools/call":
        params = req.get("params", {})
        if params.get("name") == "normalize_prompt_cache_key":
            prompt = params.get("arguments", {}).get("prompt", "")
            res = SemanticCacheKeyNormalizer.normalize_prompt_for_cache(prompt)
            return {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}
    return {"error": "Method not found"}

if __name__ == "__main__":
    for line in sys.stdin:
        if line.strip():
            print(json.dumps(handle_request(json.loads(line))))
            sys.stdout.flush()
