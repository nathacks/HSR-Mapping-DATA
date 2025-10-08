# HSR Mapping Data

This project contains Python scripts to map and transform Honkai: Star Rail game data into structured JSON outputs per
language. It is based on and uses assets compatible with StarRailRes by Mar-7th:

StarRailRes: https://github.com/Mar-7th/StarRailRes

All Python mapping scripts in this repository read raw resources (ExcelOutput and TextMap) and produce curated outputs
under data/output for multiple languages.

### Last Update: 3.6 version

## Key points

- Based on StarRailRes data format and file layout.
- Includes all Python scripts required to map, transform, and export data.
- Supports multiple languages via TextMap files.
- Outputs are deterministic and sorted for easier diffing and consumption.

## Repository layout

- data/
    - raw/ (git submodule: https://github.com/DimbreathBot/TurnBasedGameData)
        - ExcelOutput/
        - TextMap/
- output/
- src/
    - loaders/: read raw JSON from ExcelOutput and TextMap
    - transformers/: transform raw records into structured models
    - exporters/: write final JSON outputs
    - utils/: helpers (sorting, etc.)
    - main.py: entry point to run the full mapping/export pipeline
- requirements.txt
- TODO

## Raw data submodule

- The data/raw directory is a Git submodule of https://github.com/DimbreathBot/TurnBasedGameData, which contains the
  full raw Honkai: Star Rail data.
- To fetch or initialize the submodule:

  git submodule update --init --recursive

- To update it to the latest upstream revision later:

  git submodule update --remote --merge

## Requirements

- Python 3.10+ recommended
- Install dependencies:

  pip install -r requirements.txt

## Running the mapping pipeline

From the project root, run:

python -m src.main

This will read raw data and produce JSON files under data/output/<lang>/.

Notes:

- Supported languages are configured in src/config.py via the LANGUAGES list. By
  default: ["CHS", "CHT", "DE", "EN", "ES", "FR", "ID", "JP", "KR", "PT", "RU", "TH", "VI"].
- Ensure the corresponding TextMap<LANG>.json files exist in data/raw/TextMap for the languages you enable.

## Images (optional)

If you want image assets (icons, UI sprites, etc.) to be available alongside the generated data, place the spriteoutput
folder from the following repository into this project's data directory:

- Source repo: https://github.com/umaichanuwu/StarRailTextures
- Copy: StarRailTextures/spriteoutput -> data/spriteoutput

This repository reads paths like SpriteOutput/... from the raw data; having data/spriteoutput present allows these paths
to resolve to actual files locally.

### Folder structure example

Below is an example tree of the expected directories after setting up both the raw data submodule and optional images:

- data/
    - raw/ (git submodule: TurnBasedGameData)
        - ExcelOutput/
        - TextMap/
    - spriteoutput/ (optional images copied from StarRailTextures)
        - ui/
        - icon/
        - ...
- output/
    - en/
    - fr/
    - ...
- src/
    - loaders/
    - transformers/
    - exporters/
    - utils/
    - main.py
- requirements.txt
- TODO

## Outputs

Examples of generated files (per language):

- characters.json, character_promotions.json, character_skill_trees.json, character_ranks.json, character_skills.json
- light_cones.json, light_cone_promotions.json, light_cone_ranks.json
- relic_sets.json, relic_main_affixes.json, relic_sub_affixes.json, relics.json
- items.json (including books, discs), items_come_from.json
- achievements.json, descriptions.json, elements.json, paths.json, properties.json
- simulated_blessings.json, simulated_curios.json, simulated_events.json, simulated_blocks.json

Actual coverage depends on the presence of corresponding files in data/raw/ExcelOutput.

## Disclaimer

- This project is unaffiliated with HoYoverse (miHoYo) or the Honkai: Star Rail team.
- All trademarks and game content are the property of their respective owners.
- Use this project responsibly and in accordance with the licenses of the upstream resources.
