def main(): 
    name = input("What's your name? ") 
    # hello(name) 

    # printing a return value 
    print(hello(name))

# to is used in the case of empty input 
def hello(to="world"): 
    # print("hello,", to) 

    # returning instead of printing 
    return f"hello, {to}"

if __name__ == "__main__": 
    main() 