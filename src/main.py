import logging

from config import LANGUAGES
from exporters.json_exporter import export_json
from loaders.textmap_utils import load_textmap
from src.loaders.achievement_loader import load_achievements
from src.loaders.avatars_loader import load_message_contacts, load_item_player_card, \
    load_item_config_avatar_player_icon, load_item_config_avatar_player_icon_ld
from src.loaders.characters_loader import load_avatars, load_avatars_ld, load_avatar_promotions, \
    load_avatar_promotions_ld, load_avatar_skill_tree, load_avatars_enhanced, load_avatar_rank, load_avatar_rank_ld, \
    load_avatar_skill_tree_ld, load_avatar_skill, load_avatar_skill_ld, load_avatar_servant_skill
from src.loaders.description_loader import load_loading_desc
from src.loaders.elements_loader import load_damage_type
from src.loaders.items_loader import load_item, load_item_book, load_item_disk, load_item_come_from
from src.loaders.light_cone_loader import load_light_cone_promotions, load_light_cone_skill, load_light_cone, \
    load_item_light_cone
from src.loaders.paths_loader import load_avatar_base_type
from src.loaders.properties_loader import load_avatar_property
from src.loaders.relic_loader import load_relic_set, load_relic_main_affixes, load_relic_set_skill, \
    load_relic_sub_affixes, load_relic, load_item_relic
from src.loaders.simulated_loader import load_rogue_maze_buff, load_rogue_dlc_block_intro, load_rogue_miracle, \
    load_rogue_miracle_display, load_rogue_miracle_effect_display, load_rogue_talk_name, load_rogue_image
from src.transformers.achievement_transformer import transform_achievement
from src.transformers.avatars_transformer import transform_message_contacts, transform_item_player_card, \
    transform_item_config_avatar_player_icon
from src.transformers.characters_transformer import transform_avatar, transform_skill_tree_id, \
    transform_avatar_enhanced, transform_avatar_promotion, transform_avatar_rank, transform_avatar_skill_trees, \
    transform_avatar_skill
from src.transformers.descriptions_transformer import transform_descriptions
from src.transformers.elements_transformer import transform_elements
from src.transformers.items_transformer import transform_items, transform_items_come_from
from src.transformers.light_cone_transformer import transform_light_cone_promotions, transform_light_cone_ranks, \
    transform_light_cones, transform_light_cones_path
from src.transformers.nickname_transformer import transform_nickname_avatars, transform_nickname_light_cones, \
    transform_nickname_relic_set
from src.transformers.paths_transformer import transform_paths
from src.transformers.properties_transformer import transform_properties
from src.transformers.relic_transformer import transform_relic_main_affixes, transform_relic_set, \
    transform_relic_set_skill, transform_relic_sub_affixes, transform_relics, transform_item_relics
from src.transformers.simulated_transformer import transform_rogue_maze_buff, transform_rogue_block, \
    transform_rogue_miracle, transform_rogue_miracle_display, transform_rogue_miracle_effect_display, \
    transform_rogue_talk_name, transform_rogue_image
from src.utils.sorted_output import sorted_output
from transformers.generic_transformer import transformer_list

logging.basicConfig(level=logging.INFO)

TASKS = [
    {
        "name": "achievements",
        "loaders": [load_achievements],
        "transformers": transform_achievement,
        "sort": {"by": "id", "descending": False, "as_list": False},
    },
    {
        "name": "avatars",
        "loaders": [
            {"loader": load_message_contacts, "transformer": transform_message_contacts},
            {"loader": load_item_player_card, "transformer": transform_item_player_card},
            {"loader": [load_item_config_avatar_player_icon, load_item_config_avatar_player_icon_ld],
             "transformer": transform_item_config_avatar_player_icon}
        ],
        "sort": {"by": "id", "descending": False, "as_list": False},
    },
    {
        "name": "character_promotions",
        "loaders": [load_avatar_promotions, load_avatar_promotions_ld],
        "transformers": transform_avatar_promotion,
    },
    {
        "name": "character_ranks",
        "loaders": [load_avatar_rank, load_avatar_rank_ld],
        "transformers": transform_avatar_rank,
        "sort": {"by": "id", "descending": False, "as_list": False},
    },
    {
        "name": "character_skill_trees",
        "loaders": [load_avatar_skill_tree, load_avatar_skill_tree_ld],
        "transformers": transform_avatar_skill_trees,
        "sort": {"by": "id", "descending": False, "as_list": False},
    },
    {
        "name": "character_skills",
        "loaders": [load_avatar_skill, load_avatar_skill_ld, load_avatar_servant_skill],
        "transformers": transform_avatar_skill,
        "sort": {"by": "id", "descending": False, "as_list": False},
    },
    {
        "name": "characters",
        "loaders": [
            {"loader": [load_avatars, load_avatars_ld], "transformer": transform_avatar},
            {"loader": [load_avatar_skill_tree, load_avatar_skill_tree_ld], "transformer": transform_skill_tree_id},
            {"loader": load_avatars_enhanced, "transformer": transform_avatar_enhanced}
        ],
        "sort": {"by": "id", "descending": False, "as_list": False},
    },
    {
        "name": "descriptions",
        "loaders": [load_loading_desc],
        "transformers": transform_descriptions,
        "sort": {"by": "id", "descending": False, "as_list": False},
    },
    {
        "name": "elements",
        "loaders": [load_damage_type],
        "transformers": transform_elements,
    },
    {
        "name": "items",
        "loaders": [
            {"loader": [load_item, load_item_book, load_item_disk], "transformer": transform_items},
            {"loader": load_item_come_from, "transformer": transform_items_come_from}
        ],
        "sort": {"by": "id", "descending": False, "as_list": False},
    },
    {
        "name": "light_cone_promotions",
        "loaders": [load_light_cone_promotions],
        "transformers": transform_light_cone_promotions,
        "sort": {"by": "id", "descending": False, "as_list": False},
    },
    {
        "name": "light_cone_ranks",
        "loaders": [load_light_cone_skill],
        "transformers": transform_light_cone_ranks,
        "sort": {"by": "id", "descending": False, "as_list": False},
    },
    {
        "name": "light_cones",
        "loaders": [
            {"loader": load_item_light_cone, "transformer": transform_light_cones},
            {"loader": load_light_cone, "transformer": transform_light_cones_path}
        ],
        "sort": {"by": "id", "descending": False, "as_list": False},
    },
    {
        "name": "nickname",
        "loaders": [
            {"loader": [load_avatars, load_avatars_ld], "transformer": transform_nickname_avatars},
            {"loader": load_light_cone, "transformer": transform_nickname_light_cones},
            {"loader": load_relic_set, "transformer": transform_nickname_relic_set},
        ]
    },
    {
        "name": "paths",
        "loaders": [load_avatar_base_type],
        "transformers": transform_paths,
    },
    {
        "name": "properties",
        "loaders": [load_avatar_property],
        "transformers": transform_properties,
    },
    {
        "name": "relic_main_affixes",
        "loaders": [load_relic_main_affixes],
        "transformers": transform_relic_main_affixes,
    },
    {
        "name": "relic_sets",
        "loaders": [
            {"loader": load_relic_set, "transformer": transform_relic_set},
            {"loader": load_relic_set_skill, "transformer": transform_relic_set_skill},
        ]
    },
    {
        "name": "relic_sub_affixes",
        "loaders": [load_relic_sub_affixes],
        "transformers": transform_relic_sub_affixes,
    },
    {
        "name": "relics",
        "loaders": [
            {"loader": load_relic, "transformer": transform_relics},
            {"loader": load_item_relic, "transformer": transform_item_relics},
        ],
        "sort": {"by": "id", "descending": False, "as_list": False},
    },
    {
        "name": "simulated_blessings",
        "loaders": [load_rogue_maze_buff],
        "transformers": transform_rogue_maze_buff,
        "sort": {"by": "id", "descending": False, "as_list": False},
    },
    {
        "name": "simulated_blocks",
        "loaders": [load_rogue_dlc_block_intro],
        "transformers": transform_rogue_block,
        "sort": {"by": "id", "descending": False, "as_list": False},
    },
    {
        "name": "simulated_curios",
        "loaders": [
            {"loader": load_rogue_miracle, "transformer": transform_rogue_miracle},
            {"loader": load_rogue_miracle_display, "transformer": transform_rogue_miracle_display},
            {"loader": load_rogue_miracle_effect_display, "transformer": transform_rogue_miracle_effect_display},
        ],
        "sort": {"by": "id", "descending": False, "as_list": False},
    },
    {
        "name": "simulated_events",
        "loaders": [
            {"loader": load_rogue_talk_name, "transformer": transform_rogue_talk_name},
            {"loader": load_rogue_image, "transformer": transform_rogue_image},
        ],
        "sort": {"by": "id", "descending": False, "as_list": False},
    },
]


def main():
    for lang in LANGUAGES:
        logging.info(f"Processing language {lang}...")
        try:
            textmap = load_textmap(lang)
        except FileNotFoundError:
            logging.warning(f"TextMap for {lang} not found, skipping to next language.")
            continue

        for task in TASKS:
            logging.info(f"Processing {task['name']} ({lang})...")

            loaders = task.get("loaders", [])
            cumulative_result = {}

            for entry in loaders:
                if callable(entry):
                    entry = {"loader": entry, "transformer": task.get("transformers")}

                transformer = entry.get("transformer")
                loader_entry = entry.get("loader", [])

                if callable(loader_entry):
                    loader_list = [loader_entry]
                elif isinstance(loader_entry, list):
                    loader_list = loader_entry
                else:
                    loader_list = []

                loaded_data = []
                for loader_fn in loader_list:
                    try:
                        loaded = loader_fn()
                    except Exception as e:
                        logging.warning(f"Loader {loader_fn.__name__} failed: {e}")
                        continue
                    if isinstance(loaded, list) and loaded:
                        loaded_data.extend(loaded)
                    elif not isinstance(loaded, list):
                        logging.warning(f"{loader_fn.__name__} did not return a list: {type(loaded)}")

                structured_part = transformer_list(
                    loaded_data,
                    transformer,
                    textmap=textmap,
                    parent=cumulative_result
                )

                if isinstance(structured_part, dict):
                    cumulative_result.update(structured_part)
                elif isinstance(structured_part, list):
                    if not isinstance(cumulative_result, list):
                        cumulative_result = []
                    cumulative_result.extend(structured_part)
                else:
                    cumulative_result = structured_part

            structured = sorted_output(cumulative_result, task.get("sort"))
            export_json(structured, f"{task['name']}.json", lang=lang.lower())


if __name__ == "__main__":
    main()
