import argparse
from pathlib import Path
import yaml
from sys import exit

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

    print(data)

if __name__ == '__main__':
    main()
