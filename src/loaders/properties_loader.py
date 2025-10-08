from src.config import AVATAR_PROPERTY_JSON_PATH
from src.loaders.generic_loader import load_json


def load_avatar_property(filename=None):
    path = AVATAR_PROPERTY_JSON_PATH if filename is None else filename
    return load_json(path)
