import argparse
from pathlib import Path
import yaml

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
    if not config_path:
        raise Exception('No config file specified.')

    try:
        with open(config_path, 'r', encoding='utf-8') as file:
            data = yaml.safe_load(file)
    except FileNotFoundError:
        raise Exception(f'File {config_path} not found')
    except yaml.YAMLError as err:
        raise Exception(f'An error occured in the YAML file structure: {err}')

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
            