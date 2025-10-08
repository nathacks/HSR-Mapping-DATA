import re


def normalize_icon(icon_path: str) -> dict:
    icon_type = None

    icon = (
        icon_path
        .replace("SpriteOutput/SkillIcons/Avatar/", "icon/skill/")
        .replace("SpriteOutput/SkillIcons/Com/", "icon/skill/")
        .replace("SpriteOutput/UI/Avatar/Icon/", "icon/property/")
        .replace("SkillIcon_", "")
        .replace("_Normal.png", "_basic_atk.png")
        .replace("_Ultra.png", "_ultimate.png")
        .replace("_Maze.png", "_technique.png")
        .replace("_Passive.png", "_talent.png")
    )

    # Match both _BP.png and _BPxx.png
    icon = re.sub(r"_BP\d*\.png$", "_skill.png", icon)

    # Convert SkillTree → skillTreeX
    icon = re.sub(
        r'_SkillTree(\d)\.png$',
        lambda m: f"_skillTree{m.group(1)}.png",
        icon
    )

    # Servant (memosprites)
    def servant_replacer(m):
        nonlocal icon_type
        if m.group(1):  # Passive
            icon_type = "MemospriteTalent"
            return "_memosprite_talent.png"
        else:
            icon_type = "MemospriteSkill"
            return "_memosprite_skill.png"

    icon = re.sub(r"_Servant(Passive)?(\d*)\.png$", servant_replacer, icon)

    # Reduce long IDs (e.g., 1001 → 001_basic_atk)
    icon = re.sub(
        r'/(\d+)(_.*)',
        lambda m: f"/{m.group(1)[1:] + m.group(2) if len(m.group(1)) > 4 else m.group(1) + m.group(2)}",
        icon
    )

    # Remove an extra path level after "icon/skill/"
    parts = icon.split("/")
    if len(parts) > 3 and parts[1] == "skill":
        icon = "/".join(parts[:2] + parts[3:])

    return {
        "path": icon,
        "type": icon_type
    }
