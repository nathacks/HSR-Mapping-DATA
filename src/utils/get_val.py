from typing import Any


def get_val(obj: Any, default=0):
    if isinstance(obj, dict):
        return obj.get("Value", default)
    return obj if obj is not None else default
