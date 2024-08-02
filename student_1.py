def main():
    student = get_student();
    print(f"{student[0]} de {student[1]}")
    
    
def get_student():
    name = input("Enter student's name: ")
    house = input("Entrer student's house: ")
    return (name, house)


if __name__ == main():
    main()