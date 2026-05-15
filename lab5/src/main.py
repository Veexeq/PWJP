import argparse
import sys
from pathlib import Path

import config_dataclasses as cd
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

    app = cd.AppConfig(**config["app"])
    app.validate()
    app.display()

    server = cd.ServerConfig(**config["server"])
    server.validate()
    server.display()
    
    database_config = config["database"]
    credentials = cd.DatabaseCredentialsConfig(**database_config["credentials"])
    settings = cd.DatabaseSettingsConfig(**database_config["settings"])
    
    database = cd.DatabaseConfig(credentials=credentials, settings=settings)
    database.validate()
    database.display()


if __name__ == "__main__":
    main()
