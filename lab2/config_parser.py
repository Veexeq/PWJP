import argparse
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument('--config', type=Path)
args = parser.parse_args()
config_path = args.config
if not config_path:
    raise Exception('No config file specified.')

print(config_path)