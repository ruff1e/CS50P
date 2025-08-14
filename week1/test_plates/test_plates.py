from plates import is_valid



def test_plates_arg():
    assert is_valid("CS50") == "Valid"

def test_plates_no_arg():
    assert is_valid("") == "Invalid"

def test_plates_space():
    assert is_valid(" ") == "Invalid"

def test_plates_number():
    assert is_valid("123123") == "Invalid"

def test_plates_arg_letter():
    assert is_valid("C") == "Invalid"