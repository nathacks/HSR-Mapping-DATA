"""
Utility to generate a deterministic xxh64 hash from a given text.
"""

import xxhash


def hash_text_xxh64(text: str) -> str:
    """
    Generate a 64-bit xxHash from the provided text.

    Args:
        text (str): The input text to hash.

    Returns:
        str: The xxh64 hash of the text, as a string.
    """
    return str(xxhash.xxh64(text.encode("utf-8")).intdigest())
