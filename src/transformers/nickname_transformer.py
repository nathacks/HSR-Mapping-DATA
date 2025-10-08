from typing import Dict, List

from src.loaders.textmap_utils import resolve_text
from src.utils.get_hash import get_hash


def transform_nickname_avatars(raw_list: List[dict], textmap: Dict[int, str] = None, parent=None) -> Dict[str, dict]:
    result: Dict[str, dict] = {"characters": {}}

    for raw in raw_list:
        avatar_id = str(raw.get("AvatarID"))

        name_hash = get_hash(raw.get("AvatarName"))
        name = resolve_text(textmap, name_hash)

        result["characters"][avatar_id] = [name]

    return result


def transform_nickname_light_cones(raw_list: List[dict], textmap: Dict[int, str] = None, parent=None) -> Dict[
    str, dict]:
    result: Dict[str, dict] = parent.copy()

    for raw in raw_list:
        light_cone_id = str(raw.get("EquipmentID"))
        name_hash = get_hash(raw.get("EquipmentName"))
        name = resolve_text(textmap, name_hash)

        result.setdefault("light_cones", {})[light_cone_id] = [name]

    return result


def transform_nickname_relic_set(raw_list: List[dict], textmap: Dict[int, str] = None, parent=None) -> Dict[
    str, dict]:
    result: Dict[str, dict] = parent.copy()

    for raw in raw_list:
        relic_set_id = str(raw.get("SetID"))
        name_hash = get_hash(raw.get("SetName"))
        name = resolve_text(textmap, name_hash)

        result.setdefault("relic_sets", {})[relic_set_id] = [name]

    return result
