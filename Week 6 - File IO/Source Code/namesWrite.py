''' 
names = []

for _ in range(3): 
    names.append(input("What's your name? "))

for name in sorted(names): 
    print(f"hello, {name}")
'''

name = input("What's your name? ") 

# open specified file, creates one if not exists 
# "w" allows us to write, but overwrites any current files 
# "a" appends 

# file = open("names.txt", "a")
# with is another method to open and close files 
with open("names.txt", "a") as file: 
    file.write(f"{name}\n") 
# file.close() 