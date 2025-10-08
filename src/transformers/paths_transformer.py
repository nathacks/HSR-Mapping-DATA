from typing import List, Dict

from src.loaders.textmap_utils import resolve_text
from src.utils.assets import copy_sprite_to_output
from src.utils.get_hash import get_hash


def transform_paths(raw_list: List[dict], textmap: Dict[int, str] = None, parent=None) -> Dict[str, dict]:
    result: Dict[str, dict] = {}

    for raw in raw_list:
        profession_id = raw.get("ID")
        if not profession_id: continue

        text = raw.get("FirstWordText", "")

        icon_path = raw.get("BaseTypeIcon", "")
        icon_middle_path = raw.get("BaseTypeIconMiddle", "")
        icon_small_path = raw.get("BaseTypeIconSmall", "")

        name_hash = get_hash(raw.get("BaseTypeText"))
        name = resolve_text(textmap, name_hash)

        desc_hash = get_hash(raw.get("BaseTypeDesc"))
        desc = resolve_text(textmap, desc_hash)

        icon = copy_sprite_to_output(icon_path, f"icon/path/{text}.png")
        icon_middle = copy_sprite_to_output(icon_middle_path, f"icon/path/{text}Middle.png")
        icon_small = copy_sprite_to_output(icon_small_path, f"icon/path/{text}Small.png")

        result[profession_id] = {
            "id": profession_id,
            "text": text,
            "name": name,
            "desc": desc,
            "icon": icon,
            "icon_middle": icon_middle,
            "icon_small": icon_small
        }

    return result
