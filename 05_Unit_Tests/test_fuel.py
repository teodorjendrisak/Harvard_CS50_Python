import pytest
from fuel import convert, gauge

def test_convert():
    assert convert("5/6") == 83
    assert convert("1/4") == 25
    assert convert("0/1") == 0
    assert convert("1/1") == 100

def test_convert_negative():
    with pytest.raises(ValueError):
        convert("-2/6")
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ValueError):
        convert("7/6")

def test_convert_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("0/0")

def test_gauge():
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(55) == "55%"