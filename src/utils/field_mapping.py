def field_mapping(field_str: str) -> dict:
    mapping = {
        # HP
        "BaseHP": {"field": "hp", "affix": True, "ratio": False, "percent": False},
        "HPDelta": {"field": "hp", "affix": True, "ratio": False, "percent": False},
        "HPAddedRatio": {"field": "hp", "affix": True, "ratio": True, "percent": True},
        "MaxHP": {"field": "hp", "affix": False, "ratio": False, "percent": False},

        # Attack
        "BaseAttack": {"field": "atk", "affix": True, "ratio": False, "percent": False},
        "AttackDelta": {"field": "atk", "affix": True, "ratio": False, "percent": False},
        "AttackAddedRatio": {"field": "atk", "affix": True, "ratio": True, "percent": True},
        "Attack": {"field": "atk", "affix": False, "ratio": False, "percent": False},

        # Defence
        "BaseDefence": {"field": "def", "affix": True, "ratio": False, "percent": False},
        "DefenceDelta": {"field": "def", "affix": True, "ratio": False, "percent": False},
        "DefenceAddedRatio": {"field": "def", "affix": True, "ratio": True, "percent": True},
        "Defence": {"field": "def", "affix": False, "ratio": False, "percent": False},

        # Speed
        "BaseSpeed": {"field": "spd", "affix": True, "ratio": False, "percent": False},
        "SpeedDelta": {"field": "spd", "affix": True, "ratio": False, "percent": False},
        "SpeedAddedRatio": {"field": "spd", "affix": True, "ratio": True, "percent": True},
        "Speed": {"field": "spd", "affix": False, "ratio": False, "percent": False},

        # Crit
        "CriticalChanceBase": {"field": "crit_rate", "affix": True, "ratio": False, "percent": True},
        "CriticalChance": {"field": "crit_rate", "affix": False, "ratio": False, "percent": False},
        "CriticalDamageBase": {"field": "crit_dmg", "affix": True, "ratio": False, "percent": True},
        "CriticalDamage": {"field": "crit_dmg", "affix": False, "ratio": False, "percent": False},

        # Break damage
        "BreakDamageAddedRatioBase": {"field": "break_dmg", "affix": True, "ratio": False, "percent": True},
        "BreakDamageAddedRatio": {"field": "break_dmg", "affix": False, "ratio": False, "percent": False},
        "StanceBreakAddedRatio": {"field": "break_dmg", "affix": False, "ratio": False, "percent": False},

        # Healing
        "HealRatioBase": {"field": "heal_rate", "affix": True, "ratio": False, "percent": True},
        "HealRatio": {"field": "heal_rate", "affix": False, "ratio": False, "percent": True},
        "HealTakenRatio": {"field": "heal_rate", "affix": False, "ratio": False, "percent": True},

        # SP
        "SPRatioBase": {"field": "sp_rate", "affix": True, "ratio": False, "percent": True},
        "SPRatio": {"field": "sp_rate", "affix": False, "ratio": False, "percent": True},
        "MaxSP": {"field": "sp_rate", "affix": False, "ratio": False, "percent": False},
        "SpecialMaxSP": {"field": "sp_rate", "affix": False, "ratio": False, "percent": False},

        # Status
        "StatusProbabilityBase": {"field": "effect_hit", "affix": True, "ratio": False, "percent": True},
        "StatusProbability": {"field": "effect_hit", "affix": False, "ratio": False, "percent": True},
        "StatusResistanceBase": {"field": "effect_res", "affix": True, "ratio": False, "percent": True},
        "StatusResistance": {"field": "effect_res", "affix": False, "ratio": False, "percent": True},

        # Damage & Resistances
        "AllDamageTypeAddedRatio": {"field": "all_dmg", "affix": True, "ratio": False, "percent": True},

        "PhysicalAddedRatio": {"field": "physical_dmg", "affix": True, "ratio": False, "percent": True},
        "PhysicalResistance": {"field": "physical_res", "affix": True, "ratio": False, "percent": True},
        "PhysicalResistanceDelta": {"field": "physical_res", "affix": False, "ratio": False, "percent": True},

        "FireAddedRatio": {"field": "fire_dmg", "affix": True, "ratio": False, "percent": True},
        "FireResistance": {"field": "fire_res", "affix": True, "ratio": False, "percent": True},
        "FireResistanceDelta": {"field": "fire_res", "affix": False, "ratio": False, "percent": True},

        "IceAddedRatio": {"field": "ice_dmg", "affix": True, "ratio": False, "percent": True},
        "IceResistance": {"field": "ice_res", "affix": True, "ratio": False, "percent": True},
        "IceResistanceDelta": {"field": "ice_res", "affix": False, "ratio": False, "percent": True},

        "ThunderAddedRatio": {"field": "thunder_dmg", "affix": True, "ratio": False, "percent": True},
        "ThunderResistance": {"field": "thunder_res", "affix": True, "ratio": False, "percent": True},
        "ThunderResistanceDelta": {"field": "thunder_res", "affix": False, "ratio": False, "percent": True},

        "WindAddedRatio": {"field": "wind_dmg", "affix": True, "ratio": False, "percent": True},
        "WindResistance": {"field": "wind_res", "affix": True, "ratio": False, "percent": True},
        "WindResistanceDelta": {"field": "wind_res", "affix": False, "ratio": False, "percent": True},

        "QuantumAddedRatio": {"field": "quantum_dmg", "affix": True, "ratio": False, "percent": True},
        "QuantumResistance": {"field": "quantum_res", "affix": True, "ratio": False, "percent": True},
        "QuantumResistanceDelta": {"field": "quantum_res", "affix": False, "ratio": False, "percent": True},

        "ImaginaryAddedRatio": {"field": "imaginary_dmg", "affix": True, "ratio": False, "percent": True},
        "ImaginaryResistance": {"field": "imaginary_res", "affix": True, "ratio": False, "percent": True},
        "ImaginaryResistanceDelta": {"field": "imaginary_res", "affix": False, "ratio": False, "percent": True},
    }

    return mapping.get(field_str, {"field": "", "affix": False, "ratio": False, "percent": False})
