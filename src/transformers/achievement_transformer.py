from typing import Dict

from src.loaders.textmap_utils import resolve_text


def transform_achievement(raw_list: list, textmap: Dict[int, str] = None, parent=None):
    result: Dict[str, dict] = {}

    for raw in raw_list:
        achievement_id = str(raw.get("AchievementID", 0))

        title = resolve_text(textmap, raw.get("AchievementTitle", {}).get("Hash", 0))
        desc = resolve_text(textmap, raw.get("AchievementDesc", {}).get("Hash", 0))
        hide_desc = resolve_text(textmap, raw.get("AchievementDescPS", {}).get("Hash", 0))

        hide = raw.get("ShowType", "") == "ShowAfterFinish"

        result[achievement_id] = {
            "id": achievement_id,
            "series_id": str(raw.get("SeriesID", "")),
            "title": title,
            "desc": desc,
            "hide_desc": hide_desc,
            "hide": hide
        }
    return result
