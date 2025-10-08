from src.loaders.textmap_utils import resolve_text
from src.utils.assets import copy_sprite_to_output
from src.utils.rarity_mapping import rarity_mapping


def transform_message_contacts(raw_list: list, textmap: dict = None, parent=None) -> dict:
    result = {}

    for raw in raw_list:
        icon_path = raw.get("IconPath", "")
        if not icon_path:
            continue

        contact_id = str(raw.get("ID"))
        name_hash = raw.get("Name", {}).get("Hash", 0)
        name = resolve_text(textmap, name_hash)

        icon = (
            icon_path
            .replace("SpriteOutput/AvatarRoundIcon/", "icon/avatar/")
            .replace("SpriteOutput/MonsterRoundIcon/", "icon/avatar/")
            .replace("icon/avatar/Avatar", "icon/avatar/")
            .replace("icon/avatar/Series", "icon/avatar/")
        )

        icon = copy_sprite_to_output(icon_path, icon)

        result[contact_id] = {
            "id": contact_id,
            "name": name,
            "icon": icon
        }

    return result


def transform_item_player_card(raw_list: list, textmap: dict = None, parent=None) -> dict:
    result = {}

    for raw in raw_list:
        item_id = str(raw.get("ID"))
        name_hash = raw.get("ItemName", {}).get("Hash", 0)

        name = resolve_text(textmap, name_hash)

        rarity_str = raw.get("Rarity")
        rarity = rarity_mapping(rarity_str)

        icon_path = raw.get("ItemIconPath", "")
        icon = (
            icon_path
            .replace("SpriteOutput/AvatarRoundIcon/", "icon/avatar/")
            .replace("SpriteOutput/ItemIcon/AvatarHead/", "icon/avatar/")
            .replace("icon/avatar/Avatar", "icon/avatar/")
            .replace("icon/avatar/Series", "icon/avatar/")
        )
        icon = copy_sprite_to_output(icon_path, icon)

        result[item_id] = {
            "id": item_id,
            "name": name,
            "rarity": rarity,
            "icon": icon
        }

    combined = parent.copy()
    combined.update(result)
    return combined


def transform_item_config_avatar_player_icon(raw_list: list, textmap: dict = None, parent=None) -> dict:
    result = {}

    for raw in raw_list:
        item_id = str(raw.get("ID"))
        name_hash = raw.get("ItemName", {}).get("Hash", 0)

        name = resolve_text(textmap, name_hash)

        rarity_str = raw.get("Rarity")
        rarity = rarity_mapping(rarity_str)

        icon_path = raw.get("ItemIconPath", "")
        icon = (
            icon_path
            .replace("SpriteOutput/AvatarRoundIcon/Avatar/", "icon/avatar/")
            .replace("SpriteOutput/AvatarRoundIcon/Series/", "icon/avatar/")
        )
        icon = copy_sprite_to_output(icon_path, icon)

        result[item_id] = {
            "id": item_id,
            "name": name,
            "rarity": rarity,
            "icon": icon
        }

    combined = parent.copy()
    combined.update(result)
    return combined
