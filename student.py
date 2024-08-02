students = []

with open ("student.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        #print(f'{row[0]} est dans {row[1]}' )
        
        student = {"name": name, "house" : house}
        students.append(student)
        
#def get_name(student):
#    return student["name"]

#for student in sorted(students, key=get_name):
#    print(f"{student['name']} is in {student['house']}")

for student in sorted(students, key=lambda student:student["name"]):
    print(f"{student['name']} is in {student['house']}")
