# Lab 3 - Iterators and Generators

This repository contains the solutions for Laboratory 3. The project focuses on processing nested YAML configuration files using custom iterators, recursive generators, and immutable dataclasses.

## Project Structure
```text
lab3/
├── config.yaml       # Example YAML configuration file
├── parser.py         # Main script containing iterators and generators
└── README.md         # Project documentation
```

## Requirements

* Python 3.10+ (due to the use of structural pattern matching `match-case` and dataclasses with `slots=True`).
* `PyYAML` package for parsing the configuration file.

You can install the required external dependency using:
```bash
pip install PyYAML
```

## Usage

The script requires a path to a YAML configuration file passed via the `--config` argument. To run the script and see the outputs for all difficulty levels, execute the following command from the root directory:
```bash
python parser.py --config config.yaml
```
