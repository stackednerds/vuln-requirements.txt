import ast
from typing import Any

def parse_user_payload(payload: str) -> Any:
    # Replaced eval with ast.literal_eval to prevent code injection.
    return ast.literal_eval(payload)