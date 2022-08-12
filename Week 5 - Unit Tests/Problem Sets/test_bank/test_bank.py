from bank import value 
import pytest 

def test_hello(): 
    assert value("hello") == "$0"
    assert value("hello Henry") == "$0"
def test_h(): 
    assert value("hi") == "$20"
    assert value("hi Henry") == "$20"
def test_else(): 
    assert value("what's up") == "$100"
    assert value("what's up Henry") == "$100"