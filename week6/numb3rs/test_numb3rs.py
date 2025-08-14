from numb3rs import validate


def test_validate():
    assert validate("1.1.1.1") == True

def test_out_range():
    assert validate("255.255.1000.1223") == False

def test_whitespace():
    assert validate(" ") == False

def test_no_arg():
    assert validate("") == False

