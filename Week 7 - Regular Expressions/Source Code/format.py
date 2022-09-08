import re 

name = input("What's your name? ").strip() 

''' 
# in case user inputs "Yuan, Henry"
if "," in name: 
    last, first = name.split(", ") 
    name = f"{first} {last}" 
print(f"hello, {name}") 
'''

# this line can be combined, must use := (walrus operator)
if matches := re.search(r"^(.+), *(.+)$", name): 
    # last, first = matches.groups() 
    # name = f"{first} {last}" 
    name = matches.group(2) + " " + matches.group(1) 
print(f"hello, {name}")