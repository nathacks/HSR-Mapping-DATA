"""
Utility to replace parameter placeholders in a text string with formatted values.

Supports multiple formatting options for integers and percentages, e.g., #1[i], #1[f1]%.
"""

import re
from typing import List, Dict, Any


def replace_params(text: str, params: List[Dict[str, Any]]) -> str:
    """
    Replace placeholders in the text with corresponding parameter values.

    Args:
        text (str): The input string containing placeholders like #1[i], #1[f1]%, etc.
        params (List[Dict[str, Any]]): A list of parameter dictionaries, each with a "Value" key.

    Returns:
        str: The text with placeholders replaced by formatted values.
    """
    if not text:
        return ""

    for i, param in enumerate(params, start=1):
        value = param.get("Value", 0)
        replacements = [
            (rf"#{i}\[i\]%", f"{value * 100:.0f}%"),
            (rf"#{i}\[i\]", f"{int(value)}"),
            (rf"#{i}\[f1\]%", f"{value * 100:.1f}%"),
            (rf"#{i}\[f1\]", f"{value:.1f}"),
            (rf"#{i}\[f2\]%", f"{value * 100:.2f}%"),
            (rf"#{i}\[f2\]", f"{value:.2f}"),
        ]
        for pattern, repl in replacements:
            text = re.sub(pattern, repl, text)

    return text.strip()
