import argparse
from pathlib import Path
import yaml

def pretty_printer(data: dict, offset: int = 0):
    for key, val in data.items():
        indent = ' ' * offset
        if isinstance(val, dict):
            print(f'{indent}{key}:')
            pretty_printer(data=val, offset=offset + 4)
        else:
            print(f'{indent}{key}: {val}')
            
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

if __name__ == '__main__':
    main()
            