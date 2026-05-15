from enum import StrEnum
from typing import Any

import config_dataclasses as cd


class SectionType(StrEnum):
    APP = "app"
    SERVER = "server"
    DATABASE = "database"


class ConfigFactory:
    _registry: dict[str, type[cd.BaseConfigSection]] = {}

    @classmethod
    def register(
        cls, section_name: str, section_class: type[cd.BaseConfigSection]
    ) -> None:
        cls._registry[section_name] = section_class

    @classmethod
    def create_section(
        cls, section_name: str, data: dict[str, Any]
    ) -> cd.BaseConfigSection:
        section_key = section_name.lower()

        if section_name not in cls._registry:
            raise ValueError(
                f"Nieznana sekcja: '{section_name}'. Najpierw należy ją zarejestrować"
            )

        TargetClass = cls._registry[section_key]
        
        # Jeśli klasa ma własny sposób na inicjalizację, korzystamy
        if hasattr(TargetClass, 'from_dict'):
            return TargetClass.from_dict(data)
        
        return TargetClass(**data)
    
    @classmethod
    def show_registry(cls) -> str:
        return f"{cls._registry!r}"
