import re 

name = input("give your name ?").strip()

match = re.search(r"^(.+), ?(.+)$", name, re.IGNORECASE)
if match: 
    name = match.group(2) + " "+ match.group(1)
    print(name)
else:
    print("invalid")


