from bank import value


def test_bank_number():
    assert value("123") == 100

def test_bank_arg():
    assert value("hello") == 0

def test_bank_no_arg():
    assert value("") == 100

def test_bank_upper():
    assert value("HI") == 20

def test_bank_space():
    assert value(" ") == 100