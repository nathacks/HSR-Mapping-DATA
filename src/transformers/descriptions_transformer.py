from typing import Dict

from src.loaders.textmap_utils import resolve_text


def transform_descriptions(raw_list: list, textmap: Dict[int, str] = None, parent=None) -> Dict[str, dict]:
    result: Dict[str, dict] = {}

    for raw in raw_list:
        item_id = str(raw.get("ID"))

        title_hash = raw.get("TitleTextmapID", {}).get("Hash")
        desc_hash = raw.get("DescTextmapID", {}).get("Hash")
        title = resolve_text(textmap, title_hash)
        desc = resolve_text(textmap, desc_hash)

        result[item_id] = {
            "id": item_id,
            "title": title,
            "desc": desc
        }

    return result
