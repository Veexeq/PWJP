import argparse
import sys
from pathlib import Path
from typing import Any

import config_dataclasses as cd
import config_factory as cf
from config_importer import load_config


def run_basic_level(config: dict[str, Any]) -> None:
    """Prezentacja wyników dla poziomu podstawowego (Ręczne tworzenie obiektów)."""
    print("\n" + "=" * 40)
    print("POZIOM PODSTAWOWY")
    print("=" * 40)

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


def run_intermediate_level(config: dict[str, Any]) -> None:
    """Prezentacja wyników dla poziomu średniozaawansowanego (Prosta fabryka)."""
    print("\n" + "=" * 40)
    print("POZIOM ŚREDNIOZAAWANSOWANY")
    print("=" * 40)

    objects = {}
    for section_name, section_data in config.items():
        obj = cf.ConfigFactory.create_section(
            section_name=section_name, data=section_data
        )
        obj.validate()
        objects[section_name] = obj

    print("Zbudowane obiekty w słowniku:")
    for name, obj in objects.items():
        print(f" - {name}: {obj}")


def run_advanced_level(config: dict[str, Any]) -> None:
    """Prezentacja wyników dla poziomu zaawansowanego (ApplicationConfig)."""
    print("\n" + "=" * 40)
    print("POZIOM ZAAWANSOWANY")
    print("=" * 40)

    application_config = cd.ApplicationConfig()

    for section_name, section_data in config.items():
        new_section = cf.ConfigFactory.create_section(
            section_name=section_name, data=section_data
        )
        application_config.add_section(section_name=section_name, config=new_section)

    application_config.validate_all()
    application_config.display_all()


def run_bonus_level(config: dict[str, Any]) -> None:
    """Prezentacja wyników dla zadania dodatkowego (Dynamiczny Rejestr)."""
    print("\n" + "=" * 40)
    print("ZADANIE DODATKOWE (REJESTR FABRYKI)")
    print("=" * 40)

    # 1. Rejestracja klas w fabryce
    cf.ConfigFactory.register("app", cd.AppConfig)
    cf.ConfigFactory.register("server", cd.ServerConfig)
    cf.ConfigFactory.register("database", cd.DatabaseConfig)
    cf.ConfigFactory.register("logging", cd.LoggingConfig)

    # 2. Budowanie głównego obiektu przy użyciu fabryki
    application_config = cd.ApplicationConfig()

    for section_name, section_data in config.items():
        new_section = cf.ConfigFactory.create_section(
            section_name=section_name, data=section_data
        )
        application_config.add_section(section_name=section_name, config=new_section)

    # 3. Walidacja i wyświetlenie
    application_config.validate_all()
    application_config.display_all()

    # 4. Wyświetlenie stanu rejestru
    print("\n" + cf.ConfigFactory.show_registry())


def main() -> None:
    # 1. Konfiguracja CLI
    parser = argparse.ArgumentParser(description="YAML config parser")
    parser.add_argument(
        "--config", type=Path, required=True, help="Path to the YAML config file"
    )
    args = parser.parse_args()

    # 2. Wczytanie pliku
    try:
        config = load_config(args.config)
    except (FileNotFoundError, ValueError) as err:
        print(err, file=sys.stderr)
        sys.exit(1)

    # 3. Uruchamianie poszczególnych poziomów zadań (zadziała tylko ostatni poziom, bo 
    #    mam zaimplementowaną najbardziej zaawansowaną wersję fabryki z rejestrem)

    # run_basic_level(config)
    # run_intermediate_level(config)
    # run_advanced_level(config)
    run_bonus_level(config)


if __name__ == "__main__":
    main()
