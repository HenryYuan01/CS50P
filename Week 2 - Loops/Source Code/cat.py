# While loop 
'''
i = 0 
while i < 3: 
    print("meow") 
    i += 1 
'''

# For loop 
'''
for _ in range(3): 
    print("meow")
'''

# More pythonic 
''' 
print("meow\n" * 3, end="")
'''

# Ask user for number of meows 
'''
while True: 
    n = int(input("What's n? "))
    if n > 0: 
        break

for _ in range(n): 
    print("meow")
'''

# In main function 
def main(): 
    number = get_number() 
    meow(number) 

def get_number(): 
    while True: 
        n = int(input("what's n? "))
        if n > 0: 
            break 
    return n

def meow(n): 
    for _ in range(n): 
        print("meow")

main() 