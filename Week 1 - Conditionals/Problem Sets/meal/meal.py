def main():
    userTime = input("What time is it? ")
    convertedTime = convert(userTime)

    if 7 <= convertedTime <= 8: 
        print("breakfast time")
    elif 12 <= convertedTime <= 13: 
        print("lunch time")
    elif 18 <= convertedTime <= 19: 
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    minFloat = float(minutes) 
    hoursFloat = float(hours)
    convertedMin = minFloat / 60 
    return float(hoursFloat + convertedMin) 


if __name__ == "__main__":
    main()