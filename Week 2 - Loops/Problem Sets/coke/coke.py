due = 50
change = 50
total = 0 

print("Amount Due: " + str(due))

while total < 50: 
    
    coin = int(input("Insert Coin: "))

    if (coin == 25) or (coin == 10) or (coin == 5): 
        total = total + coin
        change = change - coin 
        if change <= 0: 
            break 
        else: 
            print("Amount Due: " + str(change))
    else: 
        print("Amount Due: " + str(change))

print("Change Owed: " + str(-change))