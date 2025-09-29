from bank import value

def test_value_0():
    assert value("hello") == 0

def test_value_20():
    assert value("hi") == 20
    assert value("hola") == 20

def test_value_100():
    assert value("sup") == 100
    assert value("what do you want") == 100