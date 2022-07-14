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
    # print("Too few arguments") 
    sys.exit("Too few arguments") 
''' 
elif len(sys.argv) > 2: 
    # print("Too many arguments") 
    sys.exit("Too many arguments") 
# else conditional can be removed 
'''
# allow multiple names, using slices 
for arg in sys.argv[1:]: 
    print("hello, my name is", arg) 