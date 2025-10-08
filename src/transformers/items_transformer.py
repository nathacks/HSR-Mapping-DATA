from typing import Dict

from src.loaders.textmap_utils import resolve_text
from src.utils.assets import copy_sprite_to_output
from src.utils.rarity_mapping import rarity_mapping


def transform_items(raw_list: list, textmap: Dict[int, str] = None, parent=None) -> Dict[str, dict]:
    result: Dict[str, dict] = {}

    for raw in raw_list:
        item_id = str(raw.get("ID"))
        item_type = raw.get("ItemMainType", "")
        item_sub_type = raw.get("ItemSubType", "")
        rarity = rarity_mapping(raw.get("Rarity", "Common"))

        name = ""
        if textmap and raw.get("ItemName"):
            name_hash = raw["ItemName"].get("Hash")
            if name_hash is not None:
                name = resolve_text(textmap, name_hash)

        icon = None
        icon_path = raw.get("ItemIconPath")
        if icon_path:
            icon_file = icon_path.split("/")[-1]
            icon = copy_sprite_to_output(icon_path, f"icon/item/{icon_file}")

        desc = ""
        if textmap:
            desc_hash = None
            if raw.get("ItemDesc"):
                desc_hash = raw["ItemDesc"].get("Hash")
            elif raw.get("ItemBGDesc"):
                desc_hash = raw["ItemBGDesc"].get("Hash")
            if desc_hash:
                desc = resolve_text(textmap, desc_hash).strip()

        result[item_id] = {
            "id": item_id,
            "name": name,
            "type": item_type,
            "sub_type": item_sub_type,
            "rarity": rarity,
            "icon": icon,
            "desc": desc
        }

    return result


def transform_items_come_from(raw_list: list, textmap: Dict[int, str] = None, parent=None) -> Dict[str, dict]:
    result: Dict[str, dict] = parent.copy()

    for item_id in result:
        if "come_from" not in result[item_id]:
            result[item_id]["come_from"] = []

    for raw in raw_list:
        item_id = str(raw.get("ID"))
        if item_id not in result:
            continue

        desc_text = ""
        if textmap and raw.get("Desc"):
            hash_value = raw["Desc"].get("Hash")
            if hash_value is not None:
                desc_text = resolve_text(textmap, hash_value).strip()

        if desc_text:
            result[item_id]["come_from"].append(desc_text)

    for item_id in result:
        if "come_from" in result[item_id]:
            sorted_list = sorted(
                result[item_id]["come_from"],
                key=lambda x: next(
                    (r["Sort"] for r in raw_list if
                     str(r["ID"]) == item_id and resolve_text(textmap, r["Desc"]["Hash"]).strip() == x),
                    0
                )
            )
            result[item_id]["come_from"] = sorted_list

    return result
