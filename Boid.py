import numpy as np
from datetime import date

class Boid:
    taille = 300
    def __init__(self, position = None, vitesse = None):
        self.x = (
            position if position is not None else np.random.uniform(-Boid.taille, Boid.taille, 2)
        )
        self.dx = (
            vitesse if vitesse is not None else np.random.uniform(-4, 5,2)
        )
    def __repr__(self) -> str:
        return f"Boid({self.x}, {self.dx})"
    
    def avance(self):
        self.x += self.dx
        return self 
    @property
    def vitesse(self):
        return np.linalg.norm(self.dx)
        
    @vitesse.setter
    def vitesse(self, vitesse):
        self.dx = vitesse * self.dx / self.vitesse


#a = Boid()
#print(a)
#print(a.vitesse)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __repr__(self)-> str:
        return f"Person({self.name} , {self.age})"
    
    @classmethod
    def from_Year(cls, name, Year):
        return cls(name, date.today().year - Year)
    
    def display(self):
        print(self.name + "and I am " + str(self.age))

#person1 = Person("ben", 23)
#print(person1.display())

#person2 = Person.from_Year("Ben", 2000)
#print(person2.display())

from datetime import date

# random Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def fromBirthYear(cls, name, birthYear):
        return cls(name, date.today().year - birthYear)

    def display(self):
        print(self.name + "'s age is: " + str(self.age))

person = Person('Adam', 19)
#person.display()

#person1 = Person.fromBirthYear('John',  1985)
#person1.display()