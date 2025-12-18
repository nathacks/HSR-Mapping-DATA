def get_val(value) -> int:
    """
    Retrieve a hash value from a dictionary or a raw value.

    Args:
        value (Any): The input value, which can be a dictionary or any other type.

    Returns:
        int: The extracted hash if found, otherwise 0.
    """
    if isinstance(value, dict):
        return int(value.get("Hash", 0))
    try:
        return int(value)
    except (TypeError, ValueError):
        return 0
