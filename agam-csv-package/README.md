# Agam CSV Package

A simple Python package for reading, analyzing, and getting basic statistics from CSV files.

## Features

* Read CSV files
* Get the number of rows
* Get the number of columns
* Display column names
* Detect column types
* Check missing values
* Calculate basic statistics for numerical columns
* Find top values in text columns
* Easy-to-use Python functions

## Installation

If the package is installed from PyPI:

```bash
pip install agam
```

For local development, clone the repository and install the package:

```bash
git clone <your-repository-url>
cd agam
pip install -e .
```

## Example CSV

Create a CSV file named `mydata.csv`:

```csv
Name,Age,City
Agam,20,Delhi
Anish,21,Mumbai
Rahul,22,Chandigarh
```

## Usage

Import the package in Python:

```python
import agam
```

### Get Number of Rows

```python
print(agam.rows("mydata.csv"))
```

Example output:

```text
3
```

### Get Number of Columns

```python
print(agam.columns("mydata.csv"))
```

Example output:

```text
3
```

### Get Column Names

```python
print(agam.column_names("mydata.csv"))
```

Example output:

```text
['Name', 'Age', 'City']
```

## CSV Analysis

The package can also provide basic information about the CSV file, including:

* Column names
* Data types
* Missing values
* Missing-value percentage
* Minimum value
* Mean value
* Maximum value
* Top values for text columns

Example:

```python
agam.analyze("mydata.csv")
```

Example output:

```text
Column: Age
Type: numeric
Missing: 0
Missing %: 0.0
Min: 20.0
Mean: 21.0
Max: 22.0

Column: City
Type: text
Missing: 0
Missing %: 0.0
```

## Project Structure

```text
agam-csv-package/
│
├── agam/
│   ├── __init__.py
│   └── csv_reader.py
│
├── tests/
│   └── test_csv.py
│
├── mydata.csv
├── README.md
├── pyproject.toml
└── requirements.txt
```

## Testing

The package uses `pytest` for testing.

Install pytest:

```bash
pip install pytest
```

Run the tests:

```bash
pytest
```

## Requirements

* Python 3.x
* pytest (for testing)

## Development

For local development, install the package in editable mode:

```bash
pip install -e .
```

This allows you to modify the source code and test the changes without reinstalling the package.

# Agam CSV Package

## Features

## Installation

## Usage


## Example CSV


## Output


## Testing


## Package Build


## Project Structure


## License

This project is created for learning and educational purposes.
