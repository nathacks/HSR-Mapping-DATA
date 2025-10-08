from src.config import ROGUE_MAZE_BUFF_JSON_PATH, ROGUE_DLC_BLOCK_INTRO_JSON_PATH, ROGUE_MIRACLE_JSON_PATH, \
    ROGUE_MIRACLE_DISPLAY_JSON_PATH, ROGUE_MIRACLE_EFFECT_DISPLAY_JSON_PATH, ROGUE_TALK_NAME_JSON_PATH, \
    ROGUE_IMAGE_JSON_PATH
from src.loaders.generic_loader import load_json


def load_rogue_maze_buff(filename=None):
    path = ROGUE_MAZE_BUFF_JSON_PATH if filename is None else filename
    return load_json(path)


def load_rogue_dlc_block_intro(filename=None):
    path = ROGUE_DLC_BLOCK_INTRO_JSON_PATH if filename is None else filename
    return load_json(path)


def load_rogue_miracle(filename=None):
    path = ROGUE_MIRACLE_JSON_PATH if filename is None else filename
    return load_json(path)


def load_rogue_miracle_display(filename=None):
    path = ROGUE_MIRACLE_DISPLAY_JSON_PATH if filename is None else filename
    return load_json(path)


def load_rogue_miracle_effect_display(filename=None):
    path = ROGUE_MIRACLE_EFFECT_DISPLAY_JSON_PATH if filename is None else filename
    return load_json(path)


def load_rogue_talk_name(filename=None):
    path = ROGUE_TALK_NAME_JSON_PATH if filename is None else filename
    return load_json(path)


def load_rogue_image(filename=None):
    path = ROGUE_IMAGE_JSON_PATH if filename is None else filename
    return load_json(path)
