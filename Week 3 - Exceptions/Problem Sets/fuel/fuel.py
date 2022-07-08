while True: 
    try: 
        fraction = input("Fraction: ").split('/')
        answer = (int(fraction[0]) / int(fraction[1])) * 100
        
        if answer > 100: 
            pass 
        elif answer <= 1: 
            print("E")
            break 
        elif answer >= 99: 
            print("F")
            break 
        else: 
            print(int(answer), end="")
            print("%", end="")
            break 

    except (ValueError, ZeroDivisionError): 
        pass 