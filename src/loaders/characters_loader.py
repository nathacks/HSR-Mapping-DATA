from src.config import AVATAR_JSON_PATH, AVATAR_LD_JSON_PATH, AVATAR_ENHANCED_JSON_PATH, AVATAR_PROMOTION_JSON_PATH, \
    AVATAR_PROMOTION_LD_JSON_PATH, AVATAR_SKILL_TREE_JSON_PATH, AVATAR_SKILL_TREE_LD_JSON_PATH, AVATAR_RANK_JSON_PATH, \
    AVATAR_RANK_LD_JSON_PATH, AVATAR_SKILL_JSON_PATH, AVATAR_SKILL_LD_JSON_PATH, AVATAR_SERVANT_SKILL_JSON_PATH
from src.loaders.generic_loader import load_json


def load_avatars(filename=None):
    path = AVATAR_JSON_PATH if filename is None else filename
    return load_json(path)


def load_avatars_ld(filename=None):
    path = AVATAR_LD_JSON_PATH if filename is None else filename
    return load_json(path)


def load_avatars_enhanced(filename=None):
    path = AVATAR_ENHANCED_JSON_PATH if filename is None else filename
    return load_json(path)


def load_avatar_promotions(filename=None):
    path = AVATAR_PROMOTION_JSON_PATH if filename is None else filename
    return load_json(path)


def load_avatar_promotions_ld(filename=None):
    path = AVATAR_PROMOTION_LD_JSON_PATH if filename is None else filename
    return load_json(path)


def load_avatar_skill_tree(filename=None):
    path = AVATAR_SKILL_TREE_JSON_PATH if filename is None else filename
    return load_json(path)


def load_avatar_skill_tree_ld(filename=None):
    path = AVATAR_SKILL_TREE_LD_JSON_PATH if filename is None else filename
    return load_json(path)

def load_avatar_rank(filename=None):
    path = AVATAR_RANK_JSON_PATH if filename is None else filename
    return load_json(path)

def load_avatar_rank_ld(filename=None):
    path = AVATAR_RANK_LD_JSON_PATH if filename is None else filename
    return load_json(path)

def load_avatar_skill(filename=None):
    path = AVATAR_SKILL_JSON_PATH if filename is None else filename
    return load_json(path)

def load_avatar_skill_ld(filename=None):
    path = AVATAR_SKILL_LD_JSON_PATH if filename is None else filename
    return load_json(path)

def load_avatar_servant_skill(filename=None):
    path = AVATAR_SERVANT_SKILL_JSON_PATH if filename is None else filename
    return load_json(path)
