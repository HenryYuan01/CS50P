'''
students = ["Hermione", "Harry", "Ron"]
houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]
'''

# For loop 
'''
for student in students: 
    print(student)
'''

# Length 
''' 
for i in range(len(students)): 
    print(i + 1, students[i])
'''

# Dictionary 
students = {
    "Hermione": "Gryffindor", 
    "Harry": "Gryffindor", 
    "Ron": "Gryffindor", 
    "Draco": "Slytherin"
}

# Hardcoded 
'''
print(students["Hermione"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])
'''

# Dynamically 
for student in students: 
    print(student, students[student], sep=": ")