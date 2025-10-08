from src.config import AVATAR_BASE_TYPE_JSON_PATH
from src.loaders.generic_loader import load_json


def load_avatar_base_type(filename=None):
    path = AVATAR_BASE_TYPE_JSON_PATH if filename is None else filename
    return load_json(path)
