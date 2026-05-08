import argparse
import sys
from pathlib import Path

from config_importer import load_config


def main() -> None:
    # Konfiguracja CLI
    parser = argparse.ArgumentParser(description="YAML config parser")
    parser.add_argument(
        "--config", type=Path, required=True, help="Path to the YAML config file"
    )

    args = parser.parse_args()

    try:
        config = load_config(args.config)
    except (FileNotFoundError, ValueError) as err:
        print(err, file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
