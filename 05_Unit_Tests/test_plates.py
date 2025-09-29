from plates import is_valid

def test_two_letters():
    assert is_valid("GG2222") == True
    assert is_valid("A2HDR") == False

def test_correct_length():
    assert is_valid("GGG222") == True
    assert is_valid("GGG22222") == False
    assert is_valid("2") == False

def test_numbers_end():
    assert is_valid("AAA222") == True
    assert is_valid("AA222A") == False

def test_special_character():
    assert is_valid("AAA22!") == False
    assert is_valid("A.AA22") == False