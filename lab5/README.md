# Lab 5 - Configuration Factory

This repository contains the solutions for the Configuration Factory laboratory. The project focuses on advanced Object-Oriented Programming (OOP) concepts in Python, implementing design patterns (Factory Method), Abstract Base Classes (ABC), dynamic class registration, and advanced data validation using `dataclasses`.

## Project Structure

The project has been structured to separate the configuration loading logic, factory creation, and data representations:

```text
lab5/
├── src/                      # Source code modules
│   ├── main.py               # Application entry point and CLI argument parser
│   ├── config_dataclasses.py # Dataclasses, ABCs, and validation logic for config sections
│   ├── config_factory.py     # Factory design pattern with a dynamic class registry
│   └── config_importer.py    # YAML file loading and basic structural parsing
├── config.yaml               # Sample configuration file
└── README.md                 # Project documentation
```

## Requirements

* **Python 3.11+** (due to the use of modern type hinting, `dataclasses`, `match-case` statements, and `StrEnum`).
* **PyYAML** library is required for parsing the configuration files. 

You can install the required dependencies using pip:
```bash
pip install PyYAML
```

## Running the Application

The program runs via a Command Line Interface (CLI) and requires a path to a valid YAML configuration file. To execute the main script and view the loaded, parsed, and validated configuration objects, run the following command from the root directory:

```bash
python src/main.py --config config.yaml
```

*Note: The `main.py` script is divided into distinct sections (Basic, Intermediate, Advanced, and Bonus) showcasing the progression from manual object instantiation to a fully dynamic Factory registry. All of the sections below 'Bonus' don't work because of the business logic override in `config_factory.py` file.*