"""
Utility to sort dictionary items by numeric string keys.

Non-numeric keys are ignored with a warning.
"""

from typing import Any, Dict


def sort_by_id(structured: Dict[Any, Any]) -> Dict[str, Any]:
    """
    Sort a dictionary by numeric string keys.

    Args:
        structured (Dict[Any, Any]): The dictionary to sort. Keys should be numeric strings.

    Returns:
        Dict[str, Any]: A new dictionary sorted by integer value of keys.
                        Non-numeric keys are ignored with a warning.
    """
    valid_items: Dict[str, Any] = {}

    for k, v in structured.items():
        try:
            int(k)
            valid_items[k] = v
        except (ValueError, TypeError):
            print(f"[WARNING] Non-numeric key ignored during sorting: {k}")

    # Sort dictionary by numeric value of keys
    return dict(sorted(valid_items.items(), key=lambda item: int(item[0])))
