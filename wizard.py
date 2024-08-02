class Wizard():
    def __init__(self, name, gender):
        super().__init__(name)
        super().__init__(gender)
        



class Student(Wizard):
    def __init__(self, name, house, gender):
        super().__init__(name)
        self.house = house
        super().__init__(gender)
        
        
        
        ...
        
class Professor(Wizard):
    def __init__(self, name, subject, gender):
        super().__init__(name)
        self.subject = subject 
        super().__init__(gender)

    
    def __str__(self):
        return f"{self.name} and {self.subject} and his gender {self.gender}"
        
    
    @classmethod    
    def get(cls):
        name = input("Name ")
        subject = input("subject")
        gender = input("gender")
        return cls(name, subject, gender)
    
def main():
    prof = Professor.get()
    print(f"{prof}")


if __name__ == main():
    main()