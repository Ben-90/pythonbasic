import sys


def main():
    count = 0
    check_arg()
    try:
        with open(sys.argv[1], "r") as file:
            for line in file:
                if len(line.strip()) == 0:
                    continue
                elif line.startswith('#'):
                    continue
                else:
                    count +=1
    except FileNotFoundError:
        sys.exit("File does not exist")
    print(count)


def check_arg():
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv)<2:
        sys.exit("Too few command-line arguments")
    elif '.py' not in sys.argv[1]:
        sys.exit("Not a Python file")

if __name__ == "__main__":
    main()
