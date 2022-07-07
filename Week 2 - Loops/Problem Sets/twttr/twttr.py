text = input("Input: ")

for c in text: 
    if (c.casefold() == "a") or (c.casefold() == "e") or (c.casefold() == "i") or (c.casefold() == "o") or (c.casefold() == "u"): 
        print("", end="")
    else: 
        print(c, end="")