from typing import Dict

from src.loaders.textmap_utils import resolve_text
from src.utils.assets import copy_sprite_to_output


def transform_elements(raw_list: list, textmap: Dict[int, str] = None, parent=None) -> Dict[str, dict]:
    result: Dict[str, dict] = {}

    for raw in raw_list:
        elem_id = str(raw.get("ID"))

        name_hash = raw.get("DamageTypeName", {}).get("Hash")
        desc_hash = raw.get("DamageTypeIntro", {}).get("Hash")
        name = resolve_text(textmap, name_hash)
        desc = resolve_text(textmap, desc_hash)

        icon_path = raw.get("MazeEnterBattleWeakIconPath", "")
        icon = copy_sprite_to_output(icon_path, f"icon/element/{elem_id}.png")

        color = raw.get("Color", "")

        result[elem_id] = {
            "id": elem_id,
            "name": name,
            "desc": desc,
            "color": color,
            "icon": icon
        }

    return result
