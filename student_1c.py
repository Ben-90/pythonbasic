class Student:

    def __init__(self, name, house):
        if not name:
            raise ValueError("name missing")
        self.name = name
        self.house = house
    
    def __str__(self):
        return f"{self.name} from 2 {self.house}"

    
    @classmethod
    def get(cls):
        name = input("Enter name: ")
        house = input("Enter house: ")
        return cls(name, house)
    
    
    

    

def main():
    student = Student.get()
    print(f"{student.name} from {student.house}")
    #print(student.house("ho"))


if __name__ == main():
    main()