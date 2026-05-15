from enum import StrEnum

import config_dataclasses as cd


class SectionType(StrEnum):
    APP = "app"
    SERVER = "server"
    DATABASE = "database"


class ConfigFactory:
    @staticmethod
    def create_section(section_name: str, data: dict) -> cd.BaseConfigSection:
        section = SectionType(section_name.lower())
        match section:
            case SectionType.APP:
                return cd.AppConfig(**data)
            case SectionType.SERVER:
                return cd.ServerConfig(**data)
            case SectionType.DATABASE:
                dbconfig = data["database"]
                credentials = cd.DatabaseCredentialsConfig(**dbconfig["credentials"])
                settings = cd.DatabaseSettingsConfig(**dbconfig["settings"])
                return cd.DatabaseConfig(credentials=credentials, settings=settings)
            case _:
                raise ValueError(f"{section_name} is not a valid section name")
