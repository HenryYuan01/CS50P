def main():
    fuel = input("Fraction: ").split('/')
    calculation = convert(fuel) 
    print(calculation)
    percent = gauge(calculation) 
    print(percent)


def convert(fraction):
    try: 
        calculation = (int(fraction[0]) / int(fraction[1])) * 100
        return int(calculation) 
    except (ValueError, ZeroDivisionError): 
        pass 


def gauge(percentage):
    try: 
        if int(percentage) > 100: 
            pass 
        elif int(percentage) <= 1: 
            return "E"
        elif int(percentage) >= 99: 
            return "F"
        else: 
            return(f"{int(percentage)}%")
    except (ValueError, ZeroDivisionError): 
        pass 

if __name__ == "__main__":
    main()