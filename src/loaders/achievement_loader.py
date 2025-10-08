from src.config import ACHIEVEMENT_JSON_PATH
from src.loaders.generic_loader import load_json


def load_achievements(filename=None):
    path = ACHIEVEMENT_JSON_PATH if filename is None else filename
    return load_json(path)
