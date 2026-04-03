# Lab 2: YAML Configuration Manager

This is a straightforward CLI tool built to parse, print, and validate YAML configuration files. It was developed to handle nested structures recursively and ensure all required settings are present before a program starts.

## 🛠 Setup

As mentioned in the global repository README, this project shares a common virtual environment. To install the necessary dependencies (like `PyYAML`), run the following command in the root directory:

```bash
python -m pip install -r requirements.txt
```

## ✨ What it does

* **Recursive Printing**: Walks through nested dictionaries and prints them with proper 4-space indentation.
* **YAML-friendly Formatting**: Automatically converts Python booleans to lowercase (`true`/`false`) and wraps strings in quotes for better visibility.
* **Validation**: Checks the loaded config against a list of mandatory keys, including nested ones like `database.credentials.user`.
* **Error Handling**: If the file is missing or the YAML syntax is broken, the script exits with a clear message instead of a messy traceback.

## 🚀 Usage

Run the script by pointing to your YAML file using the `--config` flag:

```bash
python config_parser.py --config config.yaml
```

### Example Output
If your config is valid, you'll see the formatted structure followed by:
`Your configuration is as expected`

If keys are missing, the tool will list exactly what's gone wrong:  
`1. database.credentials.password`  
`2. ...`


## 🔍 Required Structure

The validator expects the following keys to exist:
* **app**: `name`, `debug`
* **server**: `host`, `port`
* **database**: `credentials.user`, `credentials.password`, `settings.pool_size`, `settings.retry`

## 📁 Files
* `config_parser.py`: The main script logic.
* `config.yaml`: (Optional) Your local configuration file.

---
*Developed for the Configuration Manager laboratory assignment.*