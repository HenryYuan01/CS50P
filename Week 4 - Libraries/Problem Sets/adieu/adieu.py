import inflect 

p = inflect.engine() 

nameList = [] 

while True: 
    name = input("Name: ")
    # stop is used instead of Ctrl-D due to ^D input 
    if name == "stop": 
        break 
    else: 
        nameList.append(name)

adieuList = p.join(nameList)
print(f"Adieu, adieu, to {adieuList}")