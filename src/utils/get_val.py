def get_val(value):
    if isinstance(value, dict):
        return value.get("Value", 0)
    try:
        return float(value)
    except (TypeError, ValueError):
        return 0
