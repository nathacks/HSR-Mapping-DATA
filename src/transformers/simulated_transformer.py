from typing import Dict, List

from src.loaders.textmap_utils import resolve_text
from src.utils.assets import copy_sprite_to_output
from src.utils.get_hash import get_hash
from src.utils.replace_params import replace_params


def transform_rogue_maze_buff(raw_list: List[dict], textmap: Dict[int, str] = None, parent=None):
    result: Dict[str, dict] = {}

    for item in raw_list:
        buff_id = str(item.get("ID", ""))
        if not buff_id:
            continue

        lv = item.get("Lv", 1)
        name_hash = get_hash(item.get("BuffName"))
        name = resolve_text(textmap, name_hash)

        prev = result.get(buff_id, {})
        desc = prev.get("desc", "")
        enhanced_desc = prev.get("enhanced_desc", "")
        params = item.get("ParamList", [])

        if lv == 1:
            desc_hash = get_hash(item.get("BuffDesc"))
            raw_desc = resolve_text(textmap, desc_hash)
            desc = replace_params(raw_desc, params)

        elif lv == 2:
            enhanced_desc_hash = get_hash(item.get("BuffDescBattle"))
            raw_enhanced = resolve_text(textmap, enhanced_desc_hash)
            enhanced_desc = replace_params(raw_enhanced, params)

        entry = {
            "id": buff_id,
            "name": name,
        }

        if desc:
            entry["desc"] = desc
        if enhanced_desc:
            entry["enhanced_desc"] = enhanced_desc

        result[buff_id] = entry

    return result


def transform_rogue_block(raw_list: List[dict], textmap: Dict[int, str] = None, parent=None):
    result: Dict[str, dict] = {}

    for raw in raw_list:
        block_id = str(raw.get("BlockIntroID", ""))

        name_hash = get_hash(raw.get("BlockIntroName"))
        desc_hash = get_hash(raw.get("BlockIntroDesc"))

        name = resolve_text(textmap, name_hash)
        desc = resolve_text(textmap, desc_hash)

        icon_board = raw.get("BlockIntroIcon", "")

        def clean_icon(path: str) -> str:
            return (
                path.replace("SpriteOutput/Rogue/SceneNavi/SceneNavi", "icon/block/")
                .replace("SpriteOutput/UI/Rogue/DLC/Dice/Buff/", "icon/block/")
                .replace("SpriteOutput/UI/Rogue/DLC/RogueNous/Buff/", "icon/block/")
                .replace("SpriteOutput/Rogue/SceneNavi/", "icon/block/")
            )

        icon_board_clean = clean_icon(icon_board)
        icon = icon_board_clean.split("/")[-1]
        icon = f"icon/block/{icon}"

        icon = copy_sprite_to_output(icon_board, icon)

        color = raw.get("BlockTypeChessBoardColor", "")

        result[block_id] = {
            "id": block_id,
            "name": name,
            "desc": desc,
            "icon": icon,
            "icon_board": icon_board_clean,
            "color": color,
        }

    return result


def transform_rogue_miracle(raw_list: List[dict], textmap: Dict[int, str] = None, parent=None) -> Dict[str, dict]:
    result: Dict[str, dict] = {}
    for raw in raw_list:
        miracle_id = str(raw.get("MiracleID", "")).strip()
        display_id = raw.get("MiracleDisplayID")
        effect_id = raw.get("MiracleEffectDisplayID")

        if not display_id and not effect_id:
            continue

        result[miracle_id] = {
            "id": miracle_id,
            "displayId": str(display_id or ""),
            "effectId": str(effect_id or ""),
            "unlockHandbookMiracleId": raw.get("UnlockHandbookMiracleID"),
        }
    return result


def transform_rogue_miracle_display(raw_list: List[dict], textmap: Dict[int, str] = None, parent=None) -> Dict[
    str, dict]:
    result = (parent or {}).copy()
    display_map = {str(r.get("MiracleDisplayID")): r for r in raw_list}

    for miracle_data in result.values():
        display_raw = display_map.get(miracle_data.get("displayId", ""))
        if not display_raw:
            continue

        icon_miracle = display_raw.get("MiracleIconPath", "")
        icon = (
            icon_miracle
            .replace("SpriteOutput/Rogue/MiracleIcon/", "icon/miracle/")
            .replace("SpriteOutput/ItemIcon/", "icon/miracle/")
        )

        icon = copy_sprite_to_output(icon_miracle, icon)

        miracle_data.update({
            "name": resolve_text(textmap, get_hash(display_raw.get("MiracleName"))),
            "desc": "",
            "bg_desc": resolve_text(textmap, get_hash(display_raw.get("MiracleBGDesc"))),
            "icon": icon
        })
    return result


def transform_rogue_miracle_effect_display(raw_list: List[dict], textmap: Dict[int, str] = None, parent=None) -> Dict[
    str, dict]:
    effect_map = {str(r.get("MiracleEffectDisplayID")): r for r in raw_list}
    final_result: Dict[str, dict] = {}

    for miracle_id, miracle_data in parent.items():
        raw = effect_map.get(miracle_data.get("effectId", ""))
        desc = ""
        if raw:
            desc_text = resolve_text(textmap, get_hash(raw.get("MiracleDesc")))
            desc = replace_params(desc_text, raw.get("DescParamList", []))

        icon = miracle_data.get("icon", "")

        final_result[miracle_id] = {
            "id": miracle_data.get("id", miracle_id),
            "name": miracle_data.get("name", ""),
            "desc": desc,
            "bg_desc": miracle_data.get("bg_desc", ""),
            "icon": icon,
        }

    return final_result


def transform_rogue_talk_name(raw_list: List[dict], textmap: Dict[int, str] = None, parent=None) -> Dict[str, dict]:
    result: Dict[str, dict] = {}

    for raw in raw_list:
        talk_id = str(raw.get("TalkNameID", ""))
        image_id = str(raw.get("ImageID", ""))
        if not talk_id:
            continue

        name_hash = get_hash(raw.get("Name"))
        subname_hash = get_hash(raw.get("SubName"))

        name = resolve_text(textmap, name_hash)
        type_name = resolve_text(textmap, subname_hash)

        if name or type_name:
            result[talk_id] = {
                "id": talk_id,
                "name": name,
                "type": type_name,
                "image": image_id
            }

    return result


def transform_rogue_image(raw_list: List[dict], textmap: Dict[int, str] = None, parent: Dict[str, dict] = None) -> Dict[
    str, dict]:
    raw_image_map = {str(raw.get("ImageID", "")): raw.get("ImagePath", "") for raw in raw_list}

    for talk_id, talk_data in parent.items():
        image_id = str(talk_data.get("image", ""))
        image_path = raw_image_map.get(image_id)
        if image_path:
            filename = image_path.split("/")[-1]
            image = copy_sprite_to_output(image_path, f"image/simulated_event/{filename}")

            talk_data["image"] = image

    return parent
