from src.config import DAMAGE_TYPE_JSON_PATH
from src.loaders.generic_loader import load_json


def load_damage_type(filename=None):
    path = DAMAGE_TYPE_JSON_PATH if filename is None else filename
    return load_json(path)
