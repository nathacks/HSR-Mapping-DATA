import json
import os
import re
from typing import List

from src.config import TEXTMAP_DIR


def load_textmap(lang="FR"):
    path = os.path.join(TEXTMAP_DIR, f"TextMap{lang}.json")
    if not os.path.exists(path):
        raise FileNotFoundError(f"TextMap pour {lang} non trouvé : {path}")
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def resolve_text(textmap, hash_value):
    text = textmap.get(str(hash_value), "")
    text = text.replace("\u00A0", " ").replace("\\n", "\n").strip()
    text = re.sub(r"</?(unbreak|u)>", "", text)
    text = re.sub(r"<color=.*?>", "", text)
    text = re.sub(r"</color>", "", text)
    return text

def replace_params(desc: str, params: List[dict]) -> str:
    def replacer(match):
        index = int(match.group(1)) - 1
        if 0 <= index < len(params):
            val = params[index].get("Value")
            if isinstance(val, float):
                if 0 < val < 1:
                    return f"{int(val * 100)}%"
                return str(round(val, 2))
            return str(val)
        return match.group(0)

    return re.sub(r"#(\d+)\[i]", replacer, desc)
