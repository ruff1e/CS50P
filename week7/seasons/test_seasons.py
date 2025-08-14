from seasons import convert
import pytest
from datetime import date




def test_one_year_non_leap():
    expected = 365 * 24 * 60
    assert convert("1999-01-01", today=date(2000, 1, 1)) == expected

def test_one_year_leap():
    expected = 366 * 24 * 60
    assert convert("2000-01-01", today=date(2001, 1, 1)) == expected

def test_partial_interval():
    assert convert("1999-12-31", today=date(2000, 1, 2)) == 2 * 24 * 60

def test_invalid_empty_string():
    with pytest.raises(ValueError):
        convert("", today=date(2000, 1, 1))

def test_invalid_format_separator():
    with pytest.raises(ValueError):
        convert("1999/01/01", today=date(2000, 1, 1))

def test_nonexistent_date():
    with pytest.raises(ValueError):
        convert("2000-02-30", today=date(2001, 1, 1))

def test_future_birthdate():
    with pytest.raises(ValueError):
        convert("2001-01-02", today=date(2001, 1, 1))