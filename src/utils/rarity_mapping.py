"""
Utility to map rarity string identifiers to integer values.

This is used to normalize rarity levels in the game data, providing a numeric
representation for comparison and sorting.
"""

from typing import Dict


def rarity_mapping(rarity_str: str) -> int:
    """
    Convert a rarity string to its corresponding integer value.

    Args:
        rarity_str (str): The rarity level as a string (e.g., "SuperRare", "Normal").

    Returns:
        int: The numeric value of the rarity. Defaults to 1 (Normal) if unknown.
    """
    mapping: Dict[str, int] = {
        "SuperRare": 5,
        "VeryRare": 4,
        "Rare": 3,
        "NotNormal": 2,
        "Normal": 1,
    }
    return mapping.get(rarity_str, 1)
