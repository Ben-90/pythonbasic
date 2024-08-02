import sys
while True:
    try:
        name = input("Fraction")
        num, denum = name.split('/')
        num1, denum1 = int(num), int(denum)
        if num1> denum1:
            continue 
        s = int()
    except (ZeroDivisionError,ValueError):
        pass
    else:
        if s == 0:
            sys.exit('F')
        elif s==1:
            sys.exit('E')
        else:
            s1 = int(s*100)
            sys.exit(f'{s1}%')
        