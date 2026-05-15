import argparse
import sys
from pathlib import Path

import config_dataclasses as cd
import config_factory as cf
from config_importer import load_config


def main() -> None:
    # POZIOM PODSTAWOWY

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

    # KONIEC POZIOMU PODSTAWOWEGO

    # # POZIOM ŚREDNIOZAAWANSOWANY

    # # app_config = config["app"]
    # # section_obj = cf.ConfigFactory.create_section("app", app_config)
    # # section_obj.display()

    # # Dodatkowe założenie
    # objects = {}
    # for section_name, section_data in config.items():
    #     obj = cf.ConfigFactory.create_section(
    #         section_name=section_name, data=section_data
    #     )
    #     obj.validate()
    #     objects[section_name] = obj

    # print(str(objects))

    # # KONIEC POZIOMU ŚREDNIOZAAWANSOWANEGO

    # # POZIOM ZAAWANSOWANY

    # application_config = cd.ApplicationConfig()
    # for section_name, section_data in config.items():
    #     new_section = cf.ConfigFactory.create_section(
    #         section_name=section_name, data=section_data
    #     )
    #     application_config.add_section(section_name=section_name, config=new_section)

    # application_config.validate_all()
    # application_config.display_all()

    # # KONIEC POZIOMU ZAAWANSOWANEGO
    
    # ZADANIE DODATKOWE
    
    cf.ConfigFactory.register("app", cd.AppConfig)
    cf.ConfigFactory.register("server", cd.ServerConfig)
    cf.ConfigFactory.register("database", cd.DatabaseConfig)
    cf.ConfigFactory.register("logging", cd.LogingConfig)
    
    print(cf.ConfigFactory.show_registry())

if __name__ == "__main__":
    main()
