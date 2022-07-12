months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True: 
    tempDate = input("Date: ")
    
    if '/' in tempDate: 
        date = tempDate.split('/')
        month = int(date[0]) 
        day = int(date[1]) 
        year = int(date[2]) 

        if 1 <= month <= 12: 
            if 1 <= day <= 31: 
                if year > 0: 
                    print(year, end="-")
                    print(f"{month:02}", end="-")
                    print(f"{day:02}")
                    break 

    elif ',' in tempDate: 
        date = tempDate.replace(',', '').split(' ')
        month = int(months.index(date[0])) + 1
        day = int(date[1]) 
        year = int(date[2]) 

        if 1 <= month <= 12: 
            if 1 <= day <= 31: 
                if year > 0: 
                    print(year, end="-")
                    print(f"{month:02}", end="-")
                    print(f"{day:02}")
                    break 

    


#print(months.index(month))