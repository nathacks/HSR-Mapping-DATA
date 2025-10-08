from src.config import MESSAGE_CONTACTS_JSON_PATH, ITEM_PLAYER_CARD_JSON_PATH, ITEM_CONFIG_AVATAR_PLAYER_ICON_JSON_PATH, \
    ITEM_CONFIG_AVATAR_PLAYER_ICON_LD_JSON_PATH
from src.loaders.generic_loader import load_json


def load_message_contacts(filename=None):
    path = MESSAGE_CONTACTS_JSON_PATH if filename is None else filename
    return load_json(path)

def load_item_player_card(filename=None):
    path = ITEM_PLAYER_CARD_JSON_PATH if filename is None else filename
    return load_json(path)

def load_item_config_avatar_player_icon(filename=None):
    path = ITEM_CONFIG_AVATAR_PLAYER_ICON_JSON_PATH if filename is None else filename
    return load_json(path)

def load_item_config_avatar_player_icon_ld(filename=None):
    path = ITEM_CONFIG_AVATAR_PLAYER_ICON_LD_JSON_PATH if filename is None else filename
    return load_json(path)
