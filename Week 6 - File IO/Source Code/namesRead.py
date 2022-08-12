names = [] 


# don't actually need "r", it is default 
with open("names.txt") as file: 
    # can sort file instead 
    # for line in sorted(file): 
    for line in file: 
        # append allows sorting 
        names.append(line.rstrip()) 

        # print("hello,", line.rstrip())
    # lines = file.readlines() 

    # shorter, but can't sort 
    ''' 
    for line in file: 
        print("hello,", line.rstrip())
    '''
    

''' 
for line in lines: 
    print("hello,", line.rstrip()) 
'''

# this will sort 
for name in sorted(names): 
    print(f"hello, {name}")