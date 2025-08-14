from fuel import convert, gauge
import pytest



def test_convert():
    assert convert("2/4") == 50
    assert convert("1/4") == 25
    assert convert("3/4") == 75
    assert convert("4/4") == 100
    assert convert("0/5") == 0


def test_convert_rounding():
    assert convert("1/3") == 33
    assert convert("2/3") == 67

def test_convert_errors():
    with pytest.raises(ValueError):
        convert("percent")
    with pytest.raises(ValueError):
        convert("1/2/3")
    with pytest.raises(ValueError):
        convert("a/2")
    with pytest.raises(ValueError):
        convert("1/b")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ValueError):
        convert("5/4")
    with pytest.raises(ValueError):
        convert("-1/2")
    with pytest.raises(ValueError):
        convert("1/-2")
    with pytest.raises(ValueError):
        convert("-3/-4")


def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(2) == "2%"
    assert gauge(50) == "50%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"