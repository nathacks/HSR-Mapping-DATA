import xxhash


def hash_text_xxh64(text: str) -> str:
    return str(xxhash.xxh64(text.encode("utf-8")).intdigest())
