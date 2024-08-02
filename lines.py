import sys
count = 0
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
else:
    try:
        with open(sys.argv[1], "r") as file:
            fiche, typ = sys.argv[1].split('.')
            if typ != 'py':
                raise TypeError
            else:
                for line in file:
                    if len(line.strip()) == 0:
                        continue
                    elif line.startswith('#'):
                        continue
                    else:
                        count += 1
                    
    except IndexError:
        sys.exit("Missing command-line argument")
    except FileNotFoundError:
        sys.exit("File does not exist")
    except TypeError:
        sys.exit("Not a Python file")

print(count)

