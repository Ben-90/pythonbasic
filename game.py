import random
import sys

while True:
    try:
        level = int(input("level: "))
        if type(level) != int:
            raise ValueError
        else:
            num = random.randint(1,level)
    except ValueError:
        continue
    
    while True:
        try:
            guess = int(input("guess: "))
            if type(guess) is not int:
                raise ValueError
            elif guess > num:
                print("too large")
                continue
            elif guess < num:
                print("too small")
                continue
            else:
                print("just right")
            sys.exit()

        
        except ValueError:
            print("")

        
        
        