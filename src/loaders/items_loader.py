from src.config import ITEM_JSON_PATH, ITEM_BOOK_JSON_PATH, ITEM_DISK_JSON_PATH, ITEM_COME_FROM_JSON_PATH
from src.loaders.generic_loader import load_json


def load_item(filename=None):
    path = ITEM_JSON_PATH if filename is None else filename
    return load_json(path)


def load_item_book(filename=None):
    path = ITEM_BOOK_JSON_PATH if filename is None else filename
    return load_json(path)


def load_item_disk(filename=None):
    path = ITEM_DISK_JSON_PATH if filename is None else filename
    return load_json(path)

def load_item_come_from(filename=None):
    path = ITEM_COME_FROM_JSON_PATH if filename is None else filename
    return load_json(path)
