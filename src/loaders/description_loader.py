from src.config import LOADING_DESC_JSON_PATH
from src.loaders.generic_loader import load_json


def load_loading_desc(filename=None):
    path = LOADING_DESC_JSON_PATH if filename is None else filename
    return load_json(path)
