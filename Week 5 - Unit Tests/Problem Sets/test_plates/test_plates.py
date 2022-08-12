from plates import is_valid 
import pytest 

def test_valid(): 
    assert is_valid("CS50") == True 

def test_first_num_zero(): 
    assert is_valid("CS05") == False 

def test_letter_after_num(): 
    assert is_valid("CS50P") == False 

def test_punctuation(): 
    assert is_valid("PI3.14") == False 

def test_too_few_characters(): 
    assert is_valid("H") == False 

def test_no_nums(): 
    assert is_valid("OUTATIME") == False 