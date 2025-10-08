def sort_by_id(structured: dict):
    valid_items = {}
    for k, v in structured.items():
        try:
            int(k)
            valid_items[k] = v
        except (ValueError, TypeError):
            print(f"[WARNING] Clé non numérique ignorée lors du tri: {k}")
    return dict(sorted(valid_items.items(), key=lambda item: int(item[0])))
