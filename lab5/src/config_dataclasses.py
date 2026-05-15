from abc import ABC, abstractmethod
from dataclasses import dataclass, field, fields


class BaseConfigSection(ABC):
    def __str__(self) -> str:
        return ", ".join(
            f"{field.name}={getattr(self, field.name)!r}" for field in fields(self)
        )

    @abstractmethod
    def validate(self) -> None:
        pass

    def display(self) -> None:
        print(f"{self.__class__.__name__}: {str(self)}")


@dataclass(slots=True, frozen=False)
class ApplicationConfig:
    _sections: dict[str, BaseConfigSection] = field(default_factory=dict)

    def add_section(self, section_name: str, config: BaseConfigSection) -> None:
        self._sections[section_name] = config

    def remove_section(self, section_name: str) -> None:
        if section_name not in self.__sections:
            raise ValueError(f"{section_name} not in this ApplicationConfig")
        self._sections.pop(section_name)

    def validate_all(self) -> None:
        for section in self._sections.values():
            section.validate()

    def display_all(self) -> None:
        for name, section in self._sections.items():
            print(f"[{name}] {str(section)}")


@dataclass(slots=True, frozen=True)
class AppConfig(BaseConfigSection):
    name: str
    debug: bool

    def validate(self) -> None:
        if not isinstance(self.name, str):
            raise TypeError('"name" field must be of type "str"')
        if not isinstance(self.debug, bool):
            raise TypeError('"debug" field must be of type "bool"')
        if not self.name:
            raise ValueError('"name" field mustn\'t be empty')
        if len(self.name) < 3:
            raise ValueError('"name" field must have at least 3 letters')
        if not self.name.isalpha():
            raise ValueError('"name" must contain only letters')


@dataclass(slots=True, frozen=True)
class ServerConfig(BaseConfigSection):
    host: str
    port: int
    timeout: int

    def validate(self) -> None:
        if not isinstance(self.host, str):
            raise TypeError('"host" field must be of type "str"')
        if not isinstance(self.port, int):
            raise TypeError('"port" field must be of type "int"')
        if not isinstance(self.timeout, int):
            raise TypeError('"timeout" field must be of type "int"')
        if not self.host:
            raise ValueError('"host" field mustn\'t be empty')
        if len(self.host) < 9:
            raise ValueError('"host" field must have at least 9 characters')
        for c in self.host:
            if not c.isnumeric() and c != ".":
                raise ValueError(
                    '"host" field must contain only numbers or "." character'
                )


@dataclass(slots=True, frozen=True)
class DatabaseCredentialsConfig(BaseConfigSection):
    user: str
    password: str

    def validate(self) -> None:
        if not isinstance(self.user, str):
            raise TypeError('"user" field must be of type "str"')
        if not self.user:
            raise ValueError('"user" field mustn\'t be empty')

        if not isinstance(self.password, str):
            raise TypeError('"password" field must be of type "str"')
        if not self.password:
            raise ValueError('"password" field mustn\'t be empty')


@dataclass(slots=True, frozen=True)
class DatabaseSettingsConfig(BaseConfigSection):
    pool_size: int
    retry: bool

    def validate(self) -> None:
        if not isinstance(self.pool_size, int):
            raise TypeError('"pool_size" field must be of type "int"')
        if self.pool_size <= 0:
            raise ValueError('"pool_size" must be greater than 0')

        if not isinstance(self.retry, bool):
            raise TypeError('"retry" field must be of type "bool"')


@dataclass(slots=True, frozen=True)
class DatabaseConfig(BaseConfigSection):
    credentials: DatabaseCredentialsConfig
    settings: DatabaseSettingsConfig

    def validate(self) -> None:
        if not isinstance(self.credentials, DatabaseCredentialsConfig):
            raise TypeError(
                '"credentials" must be an instance of DatabaseCredentialsConfig'
            )
        if not isinstance(self.settings, DatabaseSettingsConfig):
            raise TypeError('"settings" must be an instance of DatabaseSettingsConfig')

        self.credentials.validate()
        self.settings.validate()


class LogingConfig(BaseConfigSection): ...
