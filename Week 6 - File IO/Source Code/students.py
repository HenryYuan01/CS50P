import csv 

students = []

with open("students.csv") as file: 
    # using CSV module 
    reader = csv.DictReader(file) 
    for row in reader: 
        students.append({"name": row["name"], "house": row["house"], "home": row["home"]})

    ''' 
    for line in file: 
        name, house, home = line.rstrip().split(",")
        
        # using dictionary 
        student = {"name": name, "house": house, "home": home} 
        students.append(student) 
    '''
    # using list 
    # students.append(f"{name} is in {house}")
    # print(f"{name} is in {home}")
''' 
for student in sorted(students): 
    print(student) 

'''

# function simply returns student name 
''' 
def get_name(student): 
    return student["name"]
'''

# sorted now works as we pass lambda key 
for student in sorted(students, key=lambda student: student["name"]): 
    print(f"{student['name']} is in {student['house']} and lives in {student['home']}")