import json
import os

from src.config import INDEX_DIR, INDEX_DIR_MIN


def export_json(data, filename, lang=None, output_dir=None):
    if output_dir is None:
        output_dir = INDEX_DIR

    pretty_dir = os.path.join(output_dir, lang.lower()) if lang else output_dir
    min_dir = os.path.join(INDEX_DIR_MIN, lang.lower()) if lang else INDEX_DIR_MIN

    os.makedirs(pretty_dir, exist_ok=True)
    os.makedirs(min_dir, exist_ok=True)

    pretty_path = os.path.join(pretty_dir, filename)
    with open(pretty_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    min_path = os.path.join(min_dir, filename)
    with open(min_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, separators=(",", ":"))

    print(f"[OK] Export to {pretty_path} and {min_path}")
