import csv


with open("students.csv") as file:
    reader = csv.reader(file)
    
    for name, house in reader:
        print(f"{name} is in {house}")
    
