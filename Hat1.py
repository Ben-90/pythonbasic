import random 

class Hat:
    
    houses = ['fann', "Gdakr", "barakami", 'MbJ']
    
    @classmethod
    def sort(cls, name):
        return f'{name} from {random.choice(cls.houses)}'

def main():
    print(Hat.sort('Mikaela'))

if __name__ == main():
    main()
    