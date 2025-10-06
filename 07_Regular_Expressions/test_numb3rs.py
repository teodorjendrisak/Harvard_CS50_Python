from numb3rs import validate

def test_length():
    assert validate("22.22.22") == False
    assert validate("22.22.22.22.22") == False
    assert validate("22.22.22.22") == True

def test_255():
    assert validate("255.255.255.255") == True
    assert validate("255.256.255.255") == False
    assert validate("0.0.0.0") == True

def test_malformed():
    assert validate("cat.dog.01.01") == False
    assert validate("01.1.1.1") == False
    assert validate("-1.1.1.1") == False