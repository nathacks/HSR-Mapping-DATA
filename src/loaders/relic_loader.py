from src.config import RELIC_SET_JSON_PATH, RELIC_MAIN_AFFIX_JSON_PATH, RELIC_SET_SKILL_JSON_PATH, \
    RELIC_SUB_AFFIX_JSON_PATH, RELIC_JSON_PATH, ITEM_RELIC_JSON_PATH
from src.loaders.generic_loader import load_json


def load_relic_set(filename=None):
    path = RELIC_SET_JSON_PATH if filename is None else filename
    return load_json(path)


def load_relic_set_skill(filename=None):
    path = RELIC_SET_SKILL_JSON_PATH if filename is None else filename
    return load_json(path)


def load_relic_main_affixes(filename=None):
    path = RELIC_MAIN_AFFIX_JSON_PATH if filename is None else filename
    return load_json(path)


def load_relic_sub_affixes(filename=None):
    path = RELIC_SUB_AFFIX_JSON_PATH if filename is None else filename
    return load_json(path)


def load_relic(filename=None):
    path = RELIC_JSON_PATH if filename is None else filename
    return load_json(path)


def load_item_relic(filename=None):
    path = ITEM_RELIC_JSON_PATH if filename is None else filename
    return load_json(path)
