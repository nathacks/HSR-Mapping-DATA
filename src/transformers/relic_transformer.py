import re
from typing import Dict

from src.loaders.textmap_utils import resolve_text
from src.utils.get_hash import get_hash
from src.utils.hash_text_xxh64 import hash_text_xxh64
from src.utils.assets import copy_sprite_to_output


def transform_relic_main_affixes(raw_list: list, textmap: Dict[int, str] = None, parent=None):
    result: Dict[str, dict] = {}

    for raw in raw_list:
        group_id = str(raw.get("GroupID"))
        affix_id = str(raw.get("AffixID"))
        prop = raw.get("Property")
        base = raw.get("BaseValue", {}).get("Value", 0)
        step = raw.get("LevelAdd", {}).get("Value", 0)

        if group_id not in result:
            result[group_id] = {
                "id": group_id,
                "affixes": {}
            }

        result[group_id]["affixes"][affix_id] = {
            "affix_id": affix_id,
            "property": prop,
            "base": base,
            "step": step
        }

    return result


def transform_relic_set(raw_list: list, textmap: Dict[int, str] = None, parent=None):
    result: Dict[str, dict] = {}

    for raw in raw_list:
        set_id = str(raw.get("SetID"))
        name_hash = get_hash(raw.get("SetName"))
        name = resolve_text(textmap, name_hash)

        icon_path = raw.get("SetIconPath", "")
        icon_base = icon_path.replace("SpriteOutput/ItemIcon/", "icon/relic/")
        icon = f"{icon_base.rsplit('/', 1)[0]}/{set_id}.png"
        if icon_path:
            icon = copy_sprite_to_output(icon_path, icon)

        result[set_id] = {
            "id": set_id,
            "name": name,
            "desc": [],
            "properties": [],
            "icon": icon
        }

    return result


def transform_relic_set_skill(raw_list: list, textmap: Dict[int, str] = None, parent=None):
    if parent is None:
        return {}

    for raw in raw_list:
        set_id = str(raw.get("SetID"))
        desc_hash = hash_text_xxh64(raw.get("SkillDesc", ""))
        property_list = raw.get("PropertyList", [])
        ability_params = raw.get("AbilityParamList", [])

        desc = resolve_text(textmap, desc_hash)

        if desc and ability_params:
            for i, param in enumerate(ability_params, start=1):
                value = param.get("Value", 0)

                desc = re.sub(rf"#{i}\[i\]%", f"{value * 100:.0f}%", desc)
                desc = re.sub(rf"#{i}\[i\]", f"{value}", desc)

        properties = []
        for prop in property_list:
            field_type = None
            value = None

            for k, v in prop.items():
                if isinstance(v, str) and not field_type:
                    field_type = v
                elif isinstance(v, dict) and "Value" in v:
                    value = v["Value"]

            if field_type and value is not None:
                properties.append({
                    "type": field_type,
                    "value": value
                })

        parent[set_id]["desc"].append(desc)
        parent[set_id]["properties"].append(properties)

    return parent


def transform_relic_sub_affixes(raw_list: list, textmap: Dict[int, str] = None, parent=None):
    result: Dict[str, dict] = {}

    for raw in raw_list:
        group_id = str(raw.get("GroupID"))
        affix_id = str(raw.get("AffixID"))

        if group_id not in result:
            result[group_id] = {
                "id": group_id,
                "affixes": {}
            }

        affix_data = {
            "affix_id": affix_id,
            "property": raw.get("Property"),
            "base": raw.get("BaseValue", {}).get("Value", 0),
            "step": raw.get("StepValue", {}).get("Value", 0),
            "step_num": raw.get("StepNum", 0)
        }

        result[group_id]["affixes"][affix_id] = affix_data

    return result


def transform_relics(raw_list: list, textmap: Dict[int, str] = None, parent=None):
    result: Dict[str, dict] = {}

    for raw in raw_list:
        relic_id = str(raw.get("ID"))
        set_id = str(raw.get("SetID"))

        rarity_str = raw.get("Rarity", "")
        rarity = int(rarity_str[-1]) if rarity_str[-1].isdigit() else 0

        result[relic_id] = {
            "id": relic_id,
            "set_id": set_id,
            "name": "",
            "rarity": rarity,
            "type": raw.get("Type"),
            "max_level": raw.get("MaxLevel"),
            "main_affix_id": str(raw.get("MainAffixGroup")),
            "sub_affix_id": str(raw.get("SubAffixGroup")),
        }

    return result


def transform_item_relics(raw_list: list, textmap: Dict[int, str] = None, parent: dict = None):
    result: Dict[str, dict] = parent.copy()

    for raw in raw_list:
        item_id = str(raw.get("ID"))

        name_hash = get_hash(raw.get("ItemName"))
        name = resolve_text(textmap, name_hash)

        set_id = result[item_id]["set_id"]

        icon_path = raw.get("ItemIconPath", "")
        match = re.search(r"IconRelic_(\d+)_(\d+)\.png", icon_path)

        index = int(match.group(2)) - 1
        icon = f"icon/relic/{set_id}_{index}.png"

        if icon_path:
            icon = copy_sprite_to_output(icon_path, icon)

        result[item_id]["name"] = name
        result[item_id]["icon"] = icon

    return result
