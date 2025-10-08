def get_hash(value):
    if isinstance(value, dict):
        return value.get("Hash", 0)
    return value or 0
