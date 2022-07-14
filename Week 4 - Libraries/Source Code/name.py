import sys 

# argv list contains file name at index 0 
# allows user to input their name at index 1 
''' 
try: 
    print("hello, my name is", sys.argv[1])
# exception added if name not provided 
except IndexError: 
    print("Too few arguments") 
'''

# another way, don't always need to resort to exception 
if len(sys.argv) < 2: 
    print("Too few arguments") 
elif len(sys.argv) > 2: 
    print("Too many arguments") 
else: 
    print("hello, my name is", sys.argv[1])