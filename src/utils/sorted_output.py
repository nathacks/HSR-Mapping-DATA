"""Utility function to sort various data structures (dict or list of dicts)
based on a configurable sorting key.
"""

from collections import OrderedDict
from typing import Any, Dict, Optional


def sorted_output(data: Any, sort_cfg: Optional[Dict[str, Any]]) -> Any:
    """Sort a given data structure according to a provided configuration.

    Args:
        data: The data to sort. Can be a dict or a list of dictionaries.
        sort_cfg: A dictionary that may contain:
            - "by": The key name to sort by.
            - "descending": Whether to sort in descending order (default: False).
            - "as_list": If True, returns a list instead of an OrderedDict.

    Returns:
        The sorted data as either a list or an OrderedDict, depending on `as_list`.
        If `sort_cfg` or `by` is missing, returns the data unchanged.
    """
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
        items = [
            (str(i.get("id", idx)), i)
            for idx, i in enumerate(data)
            if isinstance(i, dict)
        ]
    else:
        return data

    def sort_key(pair):
        """Define the key used for sorting."""
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
        items.sort(
            key=lambda p: (p[1].get(by) is None, str(p[1].get(by))),
            reverse=desc,
        )

    if as_list:
        return [it for _, it in items]

    return OrderedDict(items)
