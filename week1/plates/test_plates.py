from plates import is_valid



def test_valid_plate():
    assert is_valid("CS50") == True
    assert is_valid("AAA222") == True
    assert is_valid("AB1234") == True

def test_invalid_length():
    assert is_valid("A") == False
    assert is_valid("A1") == False
    assert is_valid("ABCDEF") == True
    assert is_valid("ABCDEFG") == False
    assert is_valid("CeEn1") == True
    assert is_valid("Koar") == True
    assert is_valid("Koars1") == True
    assert is_valid("ABC123") == True
    assert is_valid("Beem10") == True
    assert is_valid("No") == True

def test_invalid_start_letters():
    assert is_valid("0A123") == False
    assert is_valid("A1B2") == False
    assert is_valid("A") == False
    assert is_valid("AB") == True
    assert is_valid("AA") == True
    assert is_valid("A2") == False
    assert is_valid("ABC1234") == False
    assert is_valid("H1Yhre") == False
    assert is_valid("AB12CD") == False
    assert is_valid("A") == False
    assert is_valid("Bean01") == False
    assert is_valid(" Loaf!") == False
    assert is_valid("No.") == False
    assert is_valid("123ABC") == False
    assert is_valid("CS05") == False
    assert is_valid("50") == False
    assert is_valid("2A") == False
    assert is_valid("22") == False
    assert is_valid(" 2") == False      

def test_invalid_number_placement():
    assert is_valid("A0") == False
    assert is_valid("A1B2") == False
    assert is_valid("C123A") == False 

def test_invalid_characters():
    assert is_valid("C 123") == False
    assert is_valid("C.123") == False
    assert is_valid("C@123") == False