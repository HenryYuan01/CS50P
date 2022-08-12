from fuel import convert, gauge
import pytest 

def test_valid(): 
    assert convert("3/4") == 75 and gauge(75) == "75%"

def test_full(): 
    assert convert("4/4") == 100 and gauge(100) == "F"

def test_empty(): 
    assert convert("0/4") == 0 and gauge(0) == "E"