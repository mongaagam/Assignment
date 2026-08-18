from agam.csvstat import (
    rows,
    columns,
    is_numeric,
    detect_type,
    check_columns,
)

# Test number of row in csv file
def test_rows():
    assert rows("data.csv") == 5

#test  number of columns of csv file
def test_columns():
    assert columns("data.csv") == 4

#Test value is numeric or non-numeric
def test_is_numeric():
    assert is_numeric("20") is True
    assert is_numeric("hello") is False

#test the value as detected as numeric or text
def test_detect_type():
    assert detect_type(["20", "21", "22"]) == "numeric"
    assert detect_type(["Delhi", "Mumbai"]) == "text"

#print the escepted information
def test_check_columns(capsys):
    check_columns("data.csv")
    captured = capsys.readouterr()
    assert "Column:" in captured.out
    assert "Type:" in captured.out
    assert "Missing:" in captured.out
