from twttr import shorten
import pytest 
    
# no vowels 
def test_none(): 
    assert shorten("BCD") == "BCD"
    assert shorten("xyz") == "xyz"

# some vowels 
def test_some(): 
    assert shorten("DEF") == "DF" 
    assert shorten("nop") == "np"

# only vowels 
def test_all(): 
    assert shorten("AEI") == ""
    assert shorten("oui") == ""


if __name__ == "__main__":
    main()