from pathlib import Path
from typing import Any

import yaml


def load_config(config_path: Path) -> dict[str, Any]:
    """Loads and parses the YAML config file"""
    try:
        with config_path.open("r", encoding="utf-8") as file:
            config = yaml.safe_load(file)
            return config if config is not None else {}
    except FileNotFoundError:
        raise FileNotFoundError(f'Err: file "{config_path}" doesn\'t exist')
    except yaml.YAMLError as err:
        raise ValueError(f"Structural error encountered in the YAML file: {err}")
