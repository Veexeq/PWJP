import argparse
from pathlib import Path
import yaml
from sys import exit
from dataclasses import dataclass

@dataclass(slots=True, frozen=True)
class AppConfig:
    name: str
    debug: bool

@dataclass(slots=True, frozen=True)
class ServerConfig:
    host: str
    port: int
    timeout: int

@dataclass(slots=True, frozen=True)
class DatabaseConfig:
    credentials_user: str
    credentials_password: str
    settings_pool_size: int
    settings_retry: bool

@dataclass(slots=True, frozen=True)
class AppConfiguration:
    app: AppConfig
    server: ServerConfig
    database: DatabaseConfig
    
class ConfigSectionIterator:
    def __init__(self, config: dict):
        self._sections = list(config.items())
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._sections):
            raise StopIteration
        section = self._sections[self._index]
        self._index += 1
        return section

def flatten_config(config: dict, prefix: str = "") -> ...:
    for key, value in config.items():
        full_key = f'{prefix}.{key}' if prefix else key
        
        if isinstance(value, dict):
            yield from flatten_config(value, full_key)
        else:
            yield full_key, value
    
def main() -> None:
    # Parsing arguments
    parser = argparse.ArgumentParser(description='YAML config parser')
    parser.add_argument(
        '--config', 
        type=Path,
        required=True,
        help='Path to the YAML config file'
    )

    args = parser.parse_args()
    config_path = args.config

    try:
        with open(config_path, 'r', encoding='utf-8') as file:
            config = yaml.safe_load(file)
    except FileNotFoundError:
        print(f'File "{config_path}" not found')
        exit(1)
        
    except yaml.YAMLError as err:
        print(f'An error occured in the YAML file structure: {err}')
        exit(1)

    # Easy level solution
    print('\n' + '-'*15 + ' Easy Level: ' + '-'*15, '\n')
    top_level_keys = [key for key in config]
    
    print('Sekcja konfiguracji:')
    for idx, section in enumerate(config.keys()):
        print(f'[{idx}] {section}')
    
    for section_key in top_level_keys:
        section_config = config.get(section_key, {})
        
        is_nested = any(isinstance(v, dict) for v in section_config.values())
        
        if is_nested:
            continue
        
        print(f"\nSekcja '{section_key}':")
        
        keys = list(section_config.keys())
        vals = list(section_config.values())

        for k, v in zip(keys, vals):
            print(f'    {k} -> {v}')
        
    # Medium level solution
    print('\n' + '-'*15 + ' Medium Level: ' + '-'*15, '\n')
    
    gen = flatten_config(config=config)
    
    first = next(gen)
    print(f'Pierwsza wartość: {first[0]} = {first[1]}\n')
    
    print('Pozostałe pola:')
    for path, value in gen:
        print(f'   {path} = {value}')   
        
    # Hard level solution
    print('\n' + '-'*15 + ' Hard Level: ' + '-'*15, '\n')
    iterator = ConfigSectionIterator(config=config)
    
    app_cfg    = None
    server_cfg = None
    db_cfg     = None
    
    for section_name, section_data in iterator:
        print(f'Przetwarzam sekcję: {section_name}')
        
        match section_name:
            case 'app': 
                app_cfg = AppConfig(**section_data)
            case 'server':
                server_cfg = ServerConfig(**section_data)
            case 'database':
                flat_data = {k.replace('.', '_'): v for k, v in flatten_config(section_data)}
                db_cfg = DatabaseConfig(**flat_data)
    
    assert app_cfg is not None, "Brak sekcji 'app' w pliku konfiguracji!"
    assert server_cfg is not None, "Brak sekcji 'server' w pliku konfiguracji!"
    assert db_cfg is not None, "Brak sekcji 'database' w pliku konfiguracji!"
    
    main_config = AppConfiguration(app=app_cfg, server=server_cfg, database=db_cfg)
    
    print('\nKonfiguracja załadowana:')
    print(f'   {main_config.app}')
    print(f'   {main_config.server}')
    print('\nKonfiguracja jest niemutowalna — próba modyfikacji zakończy się błędem.')
    
if __name__ == '__main__':
    main()
