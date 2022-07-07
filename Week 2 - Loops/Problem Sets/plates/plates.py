from string import punctuation

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Check if length is less than 2 or greater than 6 
    if len(s) < 2 or len(s) > 6: 
        return False 
    
    # Else check if first two characters are not letters 
    elif s[0:2].isalpha() == False: 
        return False 

    # Else check if there is punctuation 
    elif any(p in s for p in punctuation): 
        return False

    # Iterate string 
    for c in s: 
        # If the character isn't a letter, it could be a number 
        if not c.isalpha(): 
            # First encounter with number, check if 0 
            if c == "0": 
                return False 
            # Otherwise valid for now, break 
            else: 
                break 
    # Knowing that a number has been encountered, and it doesn't begin with 0 
    for c in s: 
        # Check for first digit encounter 
        if c.isdigit(): 
            # Start an index count from first digit enccounter 
            index = s.index(c) 
            # Iterate from index count until end of string 
            # Check if any characters aren't digits 
            if not s[index:].isdigit(): 
                return False 

    else: 
        return True 

main()