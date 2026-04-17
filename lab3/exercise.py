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
            config = yaml.safe_load(file)
    except FileNotFoundError:
        print(f'File "{config_path}" not found')
        exit(1)
        
    except yaml.YAMLError as err:
        print(f'An error occured in the YAML file structure: {err}')
        exit(1)

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
        
if __name__ == '__main__':
    main()
