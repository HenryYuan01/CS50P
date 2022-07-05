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
''' 
students = {
    "Hermione": "Gryffindor", 
    "Harry": "Gryffindor", 
    "Ron": "Gryffindor", 
    "Draco": "Slytherin"
}
'''

# Hardcoded 
'''
print(students["Hermione"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])
'''

# Dynamically 
''' 
for student in students: 
    print(student, students[student], sep=": ")
'''

# More complex example 
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"}, 
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"}, 
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell Terrier"}, 
    {"name": "Draco", "house": "Slytherin", "patronus": None} 
]

for student in students: 
    print(student["name"], student["house"], student["patronus"], sep=", ")