def transformer_list(raw_list, transform_fn, textmap=None, parent=None):
    import json
    import logging

    normalized = []
    for i, raw in enumerate(raw_list):
        if isinstance(raw, list):
            for j, sub in enumerate(raw):
                if isinstance(sub, str):
                    try:
                        sub = json.loads(sub)
                    except json.JSONDecodeError:
                        logging.warning(f"[{i}.{j}] Non-JSON element ignored")
                        continue
                if isinstance(sub, dict):
                    normalized.append(sub)
                else:
                    logging.warning(f"[{i}.{j}] Non-dict element ignored")
            continue

        if isinstance(raw, dict):
            normalized.append(raw)
        else:
            logging.warning(f"[{i}] Non-dict element ignored")

    def _run_one(shadow_transform_fn, data, parent_data):
        try:
            result = shadow_transform_fn(data, textmap=textmap, parent=parent_data)
            if isinstance(result, dict):
                return result
            logging.warning(
                f"Transformer did not return a dict: {getattr(shadow_transform_fn, '__name__', str(shadow_transform_fn))}"
            )
        except Exception as e:
            logging.warning(
                f"Error in transformer {getattr(shadow_transform_fn, '__name__', str(shadow_transform_fn))}: {e}"
            )
        return {}

    if callable(transform_fn):
        transform_fn = [transform_fn]

    last_result = None
    for fn in transform_fn:
        last_result = _run_one(fn, normalized, parent)

    return last_result or {}
