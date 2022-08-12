def main(): 
    message = input("Input: ")
    message_no_vowels = shorten(message)
    print(message_no_vowels)

def shorten(word):
    word_no_vowels = ""
    for c in word: 
        if (c.casefold() == "a") or (c.casefold() == "e") or (c.casefold() == "i") or (c.casefold() == "o") or (c.casefold() == "u"): 
            print("", end="")
        else: 
            # print(c, end="")
            word_no_vowels += c
    return word_no_vowels 


if __name__ == "__main__":
    main()