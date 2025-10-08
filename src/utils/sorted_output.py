from typing import Any, Dict, OrderedDict


def sorted_output(data: Any, sort_cfg: Dict[str, Any] | None) -> Any:
    if not sort_cfg:
        return data

    by = sort_cfg.get("by")
    if not by:
        return data
    desc = bool(sort_cfg.get("descending", False))
    as_list = bool(sort_cfg.get("as_list", False))

    if isinstance(data, dict):
        items = list(data.items())
    elif isinstance(data, list):
        items = [(str(i.get("id", idx)), i) for idx, i in enumerate(data) if isinstance(i, dict)]
    else:
        return data

    def sort_key(pair):
        _, item = pair
        value = item.get(by)
        try:
            value = int(value)
        except (TypeError, ValueError):
            pass
        return (value is None, value)

    try:
        items.sort(key=sort_key, reverse=desc)
    except TypeError:
        items.sort(key=lambda p: (p[1].get(by) is None, str(p[1].get(by))), reverse=desc)

    if as_list:
        return [it for _, it in items]

    return OrderedDict(items)
