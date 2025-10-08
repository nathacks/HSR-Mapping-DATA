import re
from typing import List


def replace_params(text: str, params: List[dict]) -> str:
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
