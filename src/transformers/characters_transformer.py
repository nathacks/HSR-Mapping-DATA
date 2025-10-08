import re
from typing import Dict

from src.loaders.textmap_utils import resolve_text, replace_params
from src.utils.assets import copy_sprite_to_output
from src.utils.get_hash import get_hash
from src.utils.get_val import get_val
from src.utils.hash_text_xxh64 import hash_text_xxh64
from src.utils.icon_utils import normalize_icon


def transform_avatar(raw_list: list, textmap: Dict[int, str] = None, parent=None):
    result: Dict[str, dict] = {}

    for raw in raw_list:
        rarity = int(raw.get("Rarity", "CombatPowerAvatarRarityType1").replace("CombatPowerAvatarRarityType", ""))
        avatar_id = str(raw.get("AvatarID", 0))
        sp_need = raw.get("SPNeed", {}).get("Value", 0)

        name_hash = get_hash(raw.get("AvatarName"))
        name = resolve_text(textmap, name_hash)

        tag = raw.get("AvatarVOTag", "")
        path = raw.get("AvatarBaseType", "")
        element = raw.get("DamageType", "")

        ranks = [str(r) for r in raw.get("RankIDList", [])]
        skills = [str(s) for s in raw.get("SkillList", [])]

        preview = copy_sprite_to_output(f"SpriteOutput/AvatarShopIcon/Avatar/{avatar_id}.png",
                                        f"image/character_preview/{avatar_id}.png")
        portrait = copy_sprite_to_output(raw.get('AvatarCutinFrontImgPath'),
                                         f"image/character_portrait/{avatar_id}.png")

        icon = copy_sprite_to_output(raw.get('DefaultAvatarHeadIconPath'), f"icon/character/{avatar_id}.png")

        result[avatar_id] = {
            "id": avatar_id,
            "name": name,
            "tag": tag,
            "rarity": rarity,
            "path": path,
            "element": element,
            "max_sp": sp_need,
            "ranks": ranks,
            "skills": skills,
            "skill_trees": [],
            "icon": icon,
            "preview": preview,
            "portrait": portrait
        }

    return result


def transform_skill_tree_id(raw_list: list, textmap: Dict[int, str] = None, parent=None) -> Dict[str, dict]:
    skill_tree_map: Dict[str, list] = {}

    for entry in raw_list:
        avatar_id = str(entry.get("AvatarID", 0))
        point_id = str(entry.get("PointID", 0))

        if avatar_id not in skill_tree_map:
            skill_tree_map[avatar_id] = []

        if point_id not in skill_tree_map[avatar_id]:
            skill_tree_map[avatar_id].append(point_id)

    result: Dict[str, dict] = {}

    for avatar_id, raw in parent.items():
        avatar_id = str(avatar_id)
        avatar = raw.copy()

        if avatar_id in skill_tree_map:
            avatar["skill_trees"] = avatar.get("skill_trees", []) + skill_tree_map[avatar_id]

        result[avatar_id] = avatar

    return result


def transform_avatar_enhanced(raw_list: list, textmap: Dict[int, str] = None, parent=None) -> Dict[str, dict]:
    enhanced_map: Dict[str, dict] = {
        str(av["AvatarID"]): av for av in raw_list
    }

    result: Dict[str, dict] = {}

    for avatar_id, raw in parent.items():
        avatar_id = str(avatar_id)
        avatar = raw.copy()

        if avatar_id in enhanced_map:
            enhanced = enhanced_map[avatar_id]

            # rank_ids = [str(r) for r in enhanced.get("RankIDList", [])]
            # avatar["skills"] = avatar.get("skills", []) + rank_ids

            skill_ids = [str(s) for s in enhanced.get("SkillList", [])]
            avatar["skills"] = avatar.get("skills", []) + skill_ids

        result[avatar_id] = avatar

    return result


def transform_avatar_promotion(raw_list: list, textmap: Dict[int, str] = None, parent=None):
    result: Dict[str, dict] = {}

    for row in raw_list:
        avatar_id = str(row.get("AvatarID", "0"))
        if avatar_id == "0":
            continue

        promotion = int(row.get("Promotion", 0))

        entry = result.setdefault(avatar_id, {"id": avatar_id, "values": {}, "materials": {}})

        values_obj = {
            "hp": {"base": get_val(row.get("HPBase")), "step": get_val(row.get("HPAdd"))},
            "atk": {"base": get_val(row.get("AttackBase")), "step": get_val(row.get("AttackAdd"))},
            "def": {"base": get_val(row.get("DefenceBase")), "step": get_val(row.get("DefenceAdd"))},
            "spd": {"base": get_val(row.get("SpeedBase")), "step": 0},
            "taunt": {"base": get_val(row.get("BaseAggro")), "step": 0},
            "crit_rate": {"base": get_val(row.get("CriticalChance")), "step": 0},
            "crit_dmg": {"base": get_val(row.get("CriticalDamage")), "step": 0},
        }
        entry["values"][promotion] = values_obj

        mats = row.get("PromotionCostList", []) or []
        entry["materials"][promotion] = [
            {"id": str(m.get("ItemID", "")), "num": int(m.get("ItemNum", 0) or 0)}
            for m in mats
            if isinstance(m, dict) and m.get("ItemID") is not None
        ]

    for obj in result.values():
        max_promo = max(obj["values"].keys())
        obj["values"] = [obj["values"].get(i) for i in range(max_promo + 1)]
        obj["materials"] = [obj["materials"].get(i, []) for i in range(max_promo + 1)]

    return result


from typing import Dict, List


def transform_avatar_rank(raw_list: List[dict], textmap: Dict[int, str] = None, parent=None) -> Dict[str, dict]:
    result: Dict[str, dict] = {}

    for raw in raw_list:
        rank_id = str(raw.get("RankID"))

        name = raw.get("Name", "")
        desc = raw.get("Desc", "")

        name_hashed = hash_text_xxh64(name)
        desc_hash = hash_text_xxh64(desc)

        name = resolve_text(textmap, name_hashed)
        desc = resolve_text(textmap, desc_hash)

        param = raw.get("Param", [])
        desc = replace_params(desc, param)

        materials = []
        for mat in raw.get("UnlockCost", []):
            materials.append({
                "id": str(mat.get("ItemID")),
                "num": mat.get("ItemNum", 0)
            })

        level_up_skills = []
        for k, v in raw.get("SkillAddLevelList", {}).items():
            level_up_skills.append({
                "id": str(k),
                "num": v
            })

        icon_path = raw.get("IconPath", "")

        match = re.search(r"SkillIcon_(\d+)", icon_path)
        avatar_id = match.group(1)

        icon = (
            icon_path
            .replace("SpriteOutput/SkillIcons/Avatar/", "icon/skill/")
            .replace(f"icon/skill/{avatar_id}/", "icon/skill/")
            .replace("SkillIcon_", "")
        )

        icon = copy_sprite_to_output(icon_path, icon)

        result[rank_id] = {
            "id": rank_id,
            "name": name,
            "rank": raw.get("Rank"),
            "desc": desc,
            "materials": materials,
            "level_up_skills": level_up_skills,
            "icon": icon
        }

    return result


def transform_avatar_skill_trees(raw_list: List[dict], textmap: Dict[int, str] = None, parent=None) -> Dict[str, dict]:
    result: Dict[str, dict] = {}

    for raw in raw_list:
        point_id = str(raw.get("PointID"))
        max_level = raw.get("MaxLevel", 0)
        pre_points = [str(pid) for pid in raw.get("PrePoint", [])]
        anchor = raw.get("AnchorType", "")
        materials = raw.get("MaterialList", [])
        promotion = raw.get("AvatarPromotionLimit", 0)
        params = raw.get("ParamList", [])
        name = raw.get("PointName", "")
        desc = raw.get("PointDesc", "")
        skills = raw.get("LevelUpSkillID", [])
        icon_path = raw.get("IconPath", "")
        status_adds = raw.get("StatusAddList", [])

        icon_info = normalize_icon(icon_path)

        icon = icon_info["path"]
        icon = copy_sprite_to_output(icon_path, icon)

        name_hashed = hash_text_xxh64(name)
        desc_hash = hash_text_xxh64(desc)

        name = resolve_text(textmap, name_hashed)
        desc = resolve_text(textmap, desc_hash)

        mats = [
            {
                "id": str(m.get("ItemID")),
                "num": m.get("ItemNum", 0)
            }
            for m in materials
        ]

        properties = [
            {
                "type": prop.get("PropertyType", ""),
                "value": prop.get("Value", {}).get("Value", 0)
            }
            for prop in status_adds
        ]

        if point_id not in result:
            result[point_id] = {
                "id": point_id,
                "name": name or "",
                "max_level": max_level,
                "desc": desc or "",
                "params": params or [],
                "anchor": anchor,
                "pre_points": pre_points,
                "level_up_skills": [
                    {"id": str(sid), "num": 1} for sid in skills
                ],
                "levels": [],
                "icon": icon
            }

        result[point_id]["levels"].append({
            "promotion": promotion,
            "level": 0,
            "properties": properties,
            "materials": mats
        })

    for node in result.values():
        node["levels"].sort(key=lambda x: x["promotion"])

    return result


def transform_avatar_skill(raw_list: List[dict], textmap: Dict[int, str] = None, parent=None) -> Dict[str, dict]:
    result: Dict[str, dict] = {}

    for raw in raw_list:
        skill_id = str(raw.get("SkillID"))
        level = raw.get("Level", 1)

        name = resolve_text(textmap, raw.get("SkillName", {}).get("Hash"))
        simple_desc = resolve_text(textmap, raw.get("SimpleSkillDesc", {}).get("Hash"))
        desc = resolve_text(textmap, raw.get("SkillDesc", {}).get("Hash"))
        type_text = resolve_text(textmap, raw.get("SkillTypeDesc", {}).get("Hash"))
        effect_text = resolve_text(textmap, raw.get("SkillTag", {}).get("Hash"))

        icon_path = raw.get("SkillIcon", "")

        icon_info = normalize_icon(icon_path)

        icon = icon_info["path"]
        icon = copy_sprite_to_output(icon_path, icon)

        if skill_id not in result:
            result[skill_id] = {
                "id": skill_id,
                "name": name,
                "max_level": raw.get("MaxLevel", 1),
                "element": raw.get("StanceDamageType", ""),
                "type": icon_info["type"] or raw.get("AttackType", type_text),
                "type_text": type_text,
                "effect": raw.get("SkillEffect", ""),
                "effect_text": effect_text,
                "simple_desc": simple_desc,
                "desc": desc,
                "params": [],
                "icon": icon,
            }

        params = [p.get("Value") for p in raw.get("ParamList", [])]
        if params:
            while len(result[skill_id]["params"]) < level:
                result[skill_id]["params"].append([])
            result[skill_id]["params"][level - 1] = params

    return result
