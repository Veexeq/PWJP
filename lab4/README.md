# Lab 4 - Object-Oriented Programming

This repository contains the solutions for Laboratory 4. The project focuses on implementing and testing Object-Oriented Programming (OOP) concepts in Python, including encapsulation, inheritance, polymorphism, and object relations.

## Project Structure

The project has been structured to separate the source code from the test suite:
```text
lab4/
├── src/                  # Source code modules
│   ├── biblioteka.py     # Library system (relations, dataclasses)
│   ├── konto_bankowe.py  # Bank account (encapsulation, exceptions)
│   ├── pojazdy.py        # Vehicles (inheritance, polymorphism, class/static methods)
│   └── student.py        # Basic student class (magic methods)
├── tests/                # Unit tests for each module
├── pyproject.toml        # Project configuration
└── run_tests.py          # Custom test runner script
```

## Requirements

* Python 3.10+ (due to the use of modern type hinting and `dataclasses`).
* No external dependencies are required to run the core logic or tests. All modules rely on the Python Standard Library.

## Running Tests

The project uses the built-in `unittest` framework. To run the complete test suite and verify the correctness of the implemented classes, execute the following command from the root directory (`lab4/`):
```bash
python run_tests.py
```

Alternatively, you can use the standard unittest discovery module:

```bash
python -m unittest discover tests
```
