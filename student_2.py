class Student:
    
    def __init__(self, name, house):
        self.name  = name
        self.house = house
    
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    @property
    def house(self):
        return self._house
    
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Slytherin", "dakar", "fann"]:
            raise ValueError("not the good neibghour")
        self._house = house
    
    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Name cannot be empty")
        self._name = name   
        
def main():
    student = get_student()
    #print(f'{student.name} from {student.house}')
    print(student)

def get_student():
    name = input('name : ')
    house = input('house : ')
    return Student(name, house)

if __name__ == main():
    main()