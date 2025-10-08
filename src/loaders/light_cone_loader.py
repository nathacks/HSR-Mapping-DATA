from src.config import EQUIPEMENT_PROMOTION_JSON_PATH, EQUIPEMENT_SKILL_JSON_PATH, ITEM_EQUIPEMENT_CONFIG_JSON_PATH, \
    EQUIPEMENT_CONFIG_JSON_PATH
from src.loaders.generic_loader import load_json


def load_light_cone_promotions(filename=None):
    path = EQUIPEMENT_PROMOTION_JSON_PATH if filename is None else filename
    return load_json(path)


def load_light_cone_skill(filename=None):
    path = EQUIPEMENT_SKILL_JSON_PATH if filename is None else filename
    return load_json(path)

def load_item_light_cone(filename=None):
    path = ITEM_EQUIPEMENT_CONFIG_JSON_PATH if filename is None else filename
    return load_json(path)

def load_light_cone(filename=None):
    path = EQUIPEMENT_CONFIG_JSON_PATH if filename is None else filename
    return load_json(path)
