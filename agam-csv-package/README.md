# Agam CSV Package

A simple and lightweight Python package for reading CSV files and performing basic CSV analysis and statistics.

## Features

* Read CSV files
* Get the number of rows
* Get the number of columns
* Check whether a value is numeric
* Detect column data types
* Check missing values
* Calculate basic statistics for numerical columns
* Analyze text columns
* Easy-to-use Python functions

---

## Installation

### Install from PyPI

```bash
pip install agam-csv-package
```

### Install from Source

Clone the repository:

```bash
git clone <your-repository-url>
```

Go to the project directory:

```bash
cd agam-csv-package
```

Install the package in editable mode:

```bash
python -m pip install -e .
```

---

## Example CSV

Create a CSV file such as `data.csv`:

```csv
Name,Age,City
Agam,20,Delhi
Anish,21,Mumbai
Rahul,22,Chandigarh
```

---

## Usage

Import the package:

```python
import agam
```

### Get Number of Rows

```python
print(agam.rows("data.csv"))
```

Example output:

```text
Rows: 5
```

### Get Number of Columns

```python
print(agam.columns("data.csv"))
```

Example output:

```text
Columns: 4
```

### Check if a Value is Numeric

```python
print(agam.is_numeric("25"))
```

Example output:

```text
Is Numeric: True
```

---

## CSV Analysis

The package provides functions for basic CSV analysis, including:

* Row count
* Column count
* Numeric value detection
* Column type detection
* Missing-value information
* Basic numerical statistics
* Text-value analysis

You can use the available functions according to your requirements.

---

## Example

```python
import agam

print("Rows:", agam.rows("data.csv"))
print("Columns:", agam.columns("data.csv"))
print("Is Numeric:", agam.is_numeric("25"))
```

Example output:

```text
Rows: 5
Columns: 4
Is Numeric: True
```

---

## Testing

This project uses **pytest** for unit testing.

### Install pytest

```bash
python -m pip install pytest
```

### Run Tests

```bash
python -m pytest -v
```

Example:

```text
test_csvstat.py::test_rows PASSED
test_csvstat.py::test_columns PASSED
test_csvstat.py::test_is_numeric PASSED
test_csvstat.py::test_detect_type PASSED

4 passed
```

---

## Package Build

The package can be built into Python distribution files.

Build the package:

```bash
python -m build
```

The generated files will be available inside the `dist/` directory:

```text
dist/
├── agam_csv_package-0.1.0-py3-none-any.whl
└── agam_csv_package-0.1.0.tar.gz
```

---

## Project Structure

```text
agam-csv-package/
│
├── agam/
│   ├── __init__.py
│   └── csvstat.py
│
├── tests/
│   └── test_csvstat.py
│
├── data.csv
├── README.md
├── pyproject.toml
├── dist/
│   ├── agam_csv_package-0.1.0-py3-none-any.whl
│   └── agam_csv_package-0.1.0.tar.gz
└── .gitignore
```

### File Description

| File / Folder     | Purpose                                  |
| ----------------- | ---------------------------------------- |
| `agam/`           | Main Python package                      |
| `csvstat.py`      | Contains CSV functions and logic         |
| `__init__.py`     | Exposes package functions                |
| `tests/`          | Contains unit tests                      |
| `test_csvstat.py` | Tests the CSV functions                  |
| `data.csv`        | Sample CSV data                          |
| `pyproject.toml`  | Package configuration and build settings |
| `README.md`       | Project documentation                    |
| `dist/`           | Built package distributions              |
| `.gitignore`      | Files ignored by Git                     |

---

## Development

For development, install the package in editable mode:

```bash
python -m pip install -e .
```

After making changes, run the tests:

```bash
python -m pytest -v
```

Build the package:

```bash
python -m build
```

---


## License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions
