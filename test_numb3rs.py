import pytest

from numb3rs import validate

def test_true():
    assert validate("122.56.90.0") == True
    assert validate("1.2.3.2") == True
    assert validate("255.255.255.255") == True

def test_false():
    assert validate("256.1.1.1") == False
    assert validate("1.2.3") == False
    assert validate("1.2.3.256") == False
    assert validate("1.2.3.abc") == False
    assert validate("1.2.3.-1") == False
    assert validate("Bonjour") == False
    assert validate("64.128.256.512") == False 