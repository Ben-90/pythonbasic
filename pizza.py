from io import StringIO
import tabulate 
import sys
import csv


table = []
def main():
    check_arg()
    try:
        with open(sys.argv[1], "r") as file:
            reader = csv.reader(file)
            for line in reader:
                table.append(line)
            
        table

        print(tabulate.tabulate(table, tablefmt="grid"))

    
    except FileNotFoundError:
        print("File does not exist")      


def check_arg():
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv)<2:
        sys.exit("Too few command-line arguments")
    elif '.csv' not in sys.argv[1]:
        sys.exit("Not a CSV file")
        
    


if __name__ == main():
    main()