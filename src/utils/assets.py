import logging
import os
import shutil
from typing import Optional

from PIL import Image, ImageFile

from src.config import IMAGE_DIR, ENABLE_WEBP_CONVERSION, ENABLE_IMAGE, DATA_DIR

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(message)s"
)

ImageFile.LOAD_TRUNCATED_IMAGES = True


def _resolve_sprite_source(original_path: str) -> Optional[str]:
    if not original_path or not ENABLE_IMAGE:
        return None

    p = original_path.replace("\\", "/")
    lower_p = p.lower()
    marker = "spriteoutput/"
    if marker in lower_p:
        idx = lower_p.index(marker) + len(marker)
        tail = p[idx:]
    else:
        return None

    candidates = [
        os.path.join(DATA_DIR, "spriteoutput", tail),
        os.path.join(DATA_DIR, "spriteoutput", tail.lower()),
    ]

    for cand in candidates:
        if os.path.isfile(cand):
            return cand

    logging.warning(f"⚠️ No source found for: {original_path}")
    return None


def _to_webp_rel(rel_path: str) -> str:
    rel_path = rel_path.lstrip("/\\").replace("\\", "/")
    base, _ = os.path.splitext(rel_path)
    return f"{base}.webp"


def copy_sprite_to_output(original_path: str, mapped_relative: Optional[str]) -> Optional[str]:
    if not ENABLE_IMAGE:
        logging.info(f"🚫 Image handling disabled — skipping: {original_path}")
        return mapped_relative

    if not original_path or not mapped_relative:
        logging.warning(f"⛔ Invalid path: {original_path}, {mapped_relative}")
        return mapped_relative

    src = _resolve_sprite_source(original_path)
    if not src:
        return mapped_relative

    dst_png_rel = mapped_relative.lstrip("/\\").replace("\\", "/")
    dst_png_abs = os.path.join(IMAGE_DIR, dst_png_rel)

    dst_webp_rel = _to_webp_rel(mapped_relative)
    dst_webp_abs = os.path.join(IMAGE_DIR, dst_webp_rel)

    os.makedirs(os.path.dirname(dst_png_abs), exist_ok=True)

    if not os.path.exists(dst_png_abs):
        try:
            shutil.copyfile(src, dst_png_abs)
            logging.info(f"📁 Original PNG copied: {dst_png_rel}")
        except Exception as e:
            logging.error(f"❌ Failed to copy PNG: {e}")

    if not ENABLE_WEBP_CONVERSION:
        return dst_png_rel

    if not os.path.exists(dst_webp_abs):
        try:
            with Image.open(src) as im:
                has_alpha = "A" in im.getbands() or im.info.get("transparency") is not None

                im.info.pop("exif", None)
                im.info.pop("icc_profile", None)

                if has_alpha:
                    if im.mode != "RGBA":
                        im = im.convert("RGBA")
                    save_kwargs = {
                        "lossless": False,
                        "quality": 70,
                        "method": 4,
                    }
                else:
                    if im.mode != "RGB":
                        im = im.convert("RGB")
                    save_kwargs = {
                        "quality": 70,
                        "method": 4,
                        "icc_profile": None,
                    }

                im.save(dst_webp_abs, "WEBP", **save_kwargs)
                logging.info(f"✅ Converted to WEBP: {dst_webp_rel}")

        except Exception as e:
            logging.error(f"❌ WEBP conversion error: {e}")

    return dst_png_rel
