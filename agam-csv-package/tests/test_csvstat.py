from agam.csvstat import rows, columns, is_numeric, detect_type


def test_rows():
    assert rows("data.csv")==5 
def test_columns():
    assert columns("data.csv")==4
def test_is_numeric():
    assert is_numeric("20") is True
    assert is_numeric("hello") is False
def test_detect_type():
    assert detect_type(["20","21","22"]) == "numeric"
    assert detect_type(["Delhi", "Mumbai"]) == "text"
