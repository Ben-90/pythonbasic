import random 
class Hat:
    
    def __init__(self):
        self.house = ["Fann", "Griffindor", "barakani"]
    
    def sort(self, name):
        return f"{name} in {random.choice(self.house)}."
    
    


def main():
    hat = Hat()
    print(hat.sort("Ben"))
    
if __name__ == main():
    main()