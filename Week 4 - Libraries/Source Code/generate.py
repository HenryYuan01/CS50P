import random 
# from random import choice 

# coin toss 
coin = random.choice(["heads", "tails"])
# coin = choice(["heads", "tails"])
print(coin)

# pick a random number 
number = random.randint(1, 10) 
print(number)

# shuffle cards 
cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards: 
    print(card)