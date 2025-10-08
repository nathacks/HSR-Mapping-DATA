from typing import Dict, List

from src.loaders.textmap_utils import resolve_text
from src.utils.assets import copy_sprite_to_output
from src.utils.get_hash import get_hash
from src.utils.rarity_mapping import rarity_mapping


def transform_light_cone_promotions(raw_list: List[dict], textmap: Dict[int, str] = None, parent=None) -> Dict[
    str, dict]:
    result: Dict[str, dict] = {}

    for raw in raw_list:
        eq_id = str(raw.get("EquipmentID"))
        if eq_id not in result:
            result[eq_id] = {
                "id": eq_id,
                "values": [],
                "materials": []
            }

        hp = {
            "base": raw.get("BaseHP", {}).get("Value", 0),
            "step": raw.get("BaseHPAdd", {}).get("Value", 0)
        }
        atk = {
            "base": raw.get("BaseAttack", {}).get("Value", 0),
            "step": raw.get("BaseAttackAdd", {}).get("Value", 0)
        }
        defense = {
            "base": raw.get("BaseDefence", {}).get("Value", 0),
            "step": raw.get("BaseDefenceAdd", {}).get("Value", 0)
        }

        result[eq_id]["values"].append({
            "hp": hp,
            "atk": atk,
            "def": defense
        })

        promo_costs = raw.get("PromotionCostList", [])
        materials = [
            {"id": str(cost["ItemID"]), "num": cost["ItemNum"]}
            for cost in promo_costs
        ]
        result[eq_id]["materials"].append(materials)

    return result


def transform_light_cone_ranks(raw_list: List[dict], textmap: Dict[int, str] = None, parent=None) -> Dict[str, dict]:
    result: Dict[str, dict] = {}

    for raw in raw_list:
        skill_id = str(raw.get("SkillID"))

        skill_hash = get_hash(raw.get("SkillName"))
        skill = resolve_text(textmap, skill_hash)

        desc_hash = get_hash(raw.get("SkillDesc"))
        desc = resolve_text(textmap, desc_hash)

        if skill_id not in result:
            result[skill_id] = {
                "id": skill_id,
                "skill": skill,
                "desc": desc,
                "params": [],
                "properties": []
            }

        params = [p.get("Value", 0) for p in raw.get("ParamList", [])]
        result[skill_id]["params"].append(params)

        props = [
            {
                "type": prop.get("PropertyType", ""),
                "value": prop.get("Value", {}).get("Value", 0)
            }
            for prop in raw.get("AbilityProperty", [])
        ]
        result[skill_id]["properties"].append(props)

    for skill_id, data in result.items():
        if data["params"] and data["properties"]:
            combined = list(zip(data["params"], data["properties"]))
            data["params"], data["properties"] = [list(x) for x in zip(*combined)]

    return result


def transform_light_cones(raw_list: List[dict], textmap: Dict[int, str] = None, parent=None) -> Dict[str, dict]:
    result: Dict[str, dict] = {}

    for raw in raw_list:
        item_id = str(raw.get("ID", "0"))

        name_hash = get_hash(raw.get("ItemName"))
        desc_hash = get_hash(raw.get("ItemBGDesc"))

        desc = resolve_text(textmap, desc_hash)
        name = resolve_text(textmap, name_hash)

        rarity_str = raw.get("Rarity", "")
        rarity = rarity_mapping(rarity_str)

        original_icon = raw.get("ItemIconPath", "")
        original_figure = raw.get("ItemFigureIconPath", "")

        icon = original_icon.replace("SpriteOutput/ItemIcon/LightConeIcons/", "icon/light_cone/")
        preview = original_figure.replace("SpriteOutput/ItemFigures/LightCone/", "image/light_cone_preview/")
        portrait = original_figure.replace("SpriteOutput/ItemFigures/LightCone/", "image/light_cone_portrait/")

        icon = copy_sprite_to_output(original_icon, icon)
        preview = copy_sprite_to_output(original_figure, preview)
        portrait = copy_sprite_to_output(original_figure, portrait)

        result[item_id] = {
            "id": item_id,
            "name": name,
            "rarity": rarity,
            "path": "",
            "desc": desc,
            "icon": icon,
            "preview": preview,
            "portrait": portrait
        }

    return result


def transform_light_cones_path(raw_list: List[dict], textmap: Dict[int, str] = None, parent=None) -> Dict[str, dict]:
    result: Dict[str, dict] = parent.copy() if parent else {}

    for equipment_id, data in result.items():
        raw = next((r for r in raw_list if str(r.get("EquipmentID")) == equipment_id), None)

        avatar_path = raw.get("AvatarBaseType", "")
        maxRank = raw.get("MaxRank", "")
        maxPromotion = raw.get("MaxPromotion", "")

        result[equipment_id] = {
            **data,
            "path": avatar_path,
            "max_rank": maxRank,
            "max_promotion": maxPromotion
        }

    return result
