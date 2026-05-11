from typing import Any

def parse_user_payload(payload: str) -> Any:
    # Intentionally vulnerable for PoC demo only.
    return eval(payload)
