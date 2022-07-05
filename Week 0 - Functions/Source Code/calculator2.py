# Define main function 
def main(): 
    # Asking user for input 
    x = int(input("What's x? "))

    # Squaring the user's input 
    print("x squared is", square(x))

# Define square(n) function 
def square(n): 
    return n * n 

# Call main() function 
main() 