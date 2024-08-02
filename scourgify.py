import csv
import sys 

table = ['fistname, lastname, house\n']
def main():
    check_args()
    try:
        with open(sys.argv[1], "r") as file:
            reader = csv.DictReader(file, quotechar='"',delimiter=',')
            
            for row in reader:
                new_row = row["name"]+", "+row["house"]+'\n'
                table.append(new_row)
        with open(sys.argv[2], "a") as write_file:
            writer = csv.DictWriter(write_file, fieldnames=['firstname', 'lastname', 'house'], delimiter=',')
            writer.writeheader()
            writer.writerows(table)
            
    except FileNotFoundError:
        sys.exit(f"File does not exist {sys.argv[1]}")
        
def check_args():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")


if __name__ == main():
    main()