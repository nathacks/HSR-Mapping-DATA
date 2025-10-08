from typing import List, Dict

from src.loaders.textmap_utils import resolve_text
from src.utils.assets import copy_sprite_to_output
from src.utils.field_mapping import field_mapping
from src.utils.get_hash import get_hash


def transform_properties(raw_list: List[dict], textmap: Dict[int, str] = None, parent=None) -> Dict[str, dict]:
    result: Dict[str, dict] = {}

    for raw in raw_list:
        prop_type = raw.get("PropertyType", "")
        order = raw.get("Order", 0)
        icon_path = raw.get("IconPath")

        name_hash = get_hash(raw.get("PropertyName"))
        name = resolve_text(textmap, name_hash)

        icon = (
            icon_path.replace("SpriteOutput/UI/Avatar/Icon/", "icon/property/")
            if icon_path and icon_path != "0"
            else None
        )

        if icon_path and icon_path != "0":
            icon = copy_sprite_to_output(icon_path, icon)

        field_info = field_mapping(prop_type)

        result[prop_type] = {
            "type": prop_type,
            "name": name,
            **field_info,
            "order": order,
            "icon": icon,
        }

    result["SpeedAddedRatio"] = {
        "type": "SpeedAddedRatio",
        "name": resolve_text(textmap, 6046473057757335895),
        "field": "spd",
        "affix": True,
        "ratio": True,
        "percent": True,
        "order": 100,
        "icon": "icon/property/IconSpeed.png"
    }

    result["AllDamageTypeAddedRatio"] = {
        "type": "AllDamageTypeAddedRatio",
        "name": resolve_text(textmap, 2872515639890914041),
        "field": "all_dmg",
        "affix": True,
        "ratio": False,
        "percent": True,
        "order": 101,
        "icon": "icon/property/IconAttack.png"
    }

    return result
