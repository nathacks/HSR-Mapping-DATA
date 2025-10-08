import json
import os


def load_json(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} not found.")
    with open(file_path, encoding="utf-8") as f:
        return json.load(f)
