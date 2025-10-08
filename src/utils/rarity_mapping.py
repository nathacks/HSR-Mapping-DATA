def rarity_mapping(rarity_str: str) -> int:
    mapping = {
        "SuperRare": 5,
        "VeryRare": 4,
        "Rare": 3,
        "NotNormal": 2,
        "Normal": 1,
    }
    return mapping.get(rarity_str, 1)
