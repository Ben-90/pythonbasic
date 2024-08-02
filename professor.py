import random

def main():
    print(generate_integer())


def get_level():
    while True:
        try:
            level = int(input("level: "))
            if type(level) is not int:
                raise TypeError
            elif level < 1 or level > 3:
                raise ValueError
            else:
                return level
        except ValueError:
            continue
        except TypeError:
            continue
        
        

def generate_integer():
    score = 0
    level = get_level()
    
    for i in range(10):
        
        if level == 1:  
            number1 = random.randint(0, 9)
            number2 = random.randint(0, 9)
        elif level == 2:
            number1 = random.randint(10, 99)
            number2 = random.randint(10, 99)
        else:
            number1 = random.randint(100, 999)
            number2 = random.randint(100, 999)
        
        compt = 0
        
        try:
            answer = int(input(f'{number1} + {number2} = '))
            
            if type(answer) is not int:
                raise TypeError
            elif answer == number1 + number2:
                score += 1
            else:
                while compt < 2:
                    print('EEE')
                    answer = int(input(f'{number1} + {number2} = '))
                    compt += 1
                print(f'{number1} + {number2} = {number1+number2}')
                
        except (TypeError, ValueError):
            pass
    return score




if __name__ == "__main__":
    main()