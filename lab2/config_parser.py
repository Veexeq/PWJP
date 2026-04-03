import argparse
from pathlib import Path
import yaml
from sys import exit

REQUIRED_PATHS: list[str] = [
        'app.name',
        'app.debug',
        'server.host',
        'server.port',
        'database.credentials.user',
        'database.credentials.password',
        'database.settings.pool_size',
        'database.settings.retry',
    ]

def pretty_printer(data: dict, offset: int = 0) -> None:
    for key, val in data.items():
        indent = ' ' * offset
        if isinstance(val, dict):
            print(f'{indent}{key}:')
            pretty_printer(data=val, offset=offset + 4)
        else:
            # bool in Python is capitalized, and in YAML is all lowercase
            if isinstance(val, bool):
                val = str(val).lower()
            # strings in YAML are surrounded with ""
            elif isinstance(val, str):
                val = f'"{val}"'
                
            print(f'{indent}{key}: {val}')
            
def config_validator(data: dict) -> list[str] | None:
    missing_paths: set[str] = set()
    
    for path in REQUIRED_PATHS:
        steps = path.split('.')
        
        curr_dict = data
        for idx, step in enumerate(steps):
            try:
                curr_dict = curr_dict[step]
            except KeyError:
                missing_paths.add('.'.join(steps[:idx + 1]))
        
    return sorted(list(missing_paths))
            
def main() -> None:
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
            data = yaml.safe_load(file)
    except FileNotFoundError:
        print(f'File "{config_path}" not found')
        exit(1)
        
    except yaml.YAMLError as err:
        print(f'An error occured in the YAML file structure: {err}')
        exit(1)

    pretty_printer(data=data)
    print()
    
    missing_paths = config_validator(data=data)
    if not missing_paths:
        print('Your configuration is as expected')
    else:
        print('Your configuration is missing paths listed below:')
        for idx, path in enumerate(missing_paths):
            print(f'{idx + 1}. {path}')

if __name__ == '__main__':
    main()
            