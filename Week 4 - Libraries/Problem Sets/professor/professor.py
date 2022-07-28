import random

def main():
    score = 0 
    level = get_level() 

    for i in range(10): 
        question = generate_integer(level)
        wrongCount = 0 

        while True: 
            answer = input(f"{question[0]} + {question[1]} = ")

            if int(answer) == (question[0] + question[1]): 
                score = score + 1
                break 
            else: 
                if wrongCount == 2: 
                    print("EEE")
                    print(f"{question[0]} + {question[1]} = {question[0] + question[1]}")
                    break 
                else: 
                    print("EEE") 
                    wrongCount = wrongCount + 1 
                    pass 
    
    print(f"Score: {score}")



def get_level():
    while True: 
        level = int(input("Level: "))

        if level == 1 or level == 2 or level == 3: 
            return level 

def generate_integer(level):
    if level == 1: 
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        return x, y 
    elif level == 2: 
        x = random.randint(10, 99)
        y = random.randint(10, 99)
        return x, y 
    else: 
        x = random.randint(100, 999)
        y = random.randint(100, 999)
        return x, y 

if __name__ == "__main__":
    main()