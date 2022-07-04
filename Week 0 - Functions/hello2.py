def main(): 
    # Ask the user for their name
    name = input("What's your name? ") 

    # Call hello() function with user's name 
    hello(name) 

# Define the hello() function 
def hello(to="world"): 
    print("hello,", to) 

main() 