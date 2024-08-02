import datetime
mouths = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    try:
        date = input("Date: ")
        if "/" in date:
            mouth, day, year = date.split("/")
            if int(mouth) > 12 or int(day) > 31:
                raise ValueError
            else:
                print(f"{year}-{int(mouth) - 1}-{day}")
                break
        elif " " in date:
            date = date.replace(" ", ",")
            mouth, day, year = date.split(",")
            mouth = mouth.title()
            if mouth not in mouths or int(day) > 31:
                raise ValueError
            else:
                print(f"{year}-{mouths.index(mouth)+1}-{day}")
                break
        else:
            continue
    except ValueError:
        continue



            
            