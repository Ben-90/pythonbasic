
import re

email = input('your email ?').strip()

if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
    print(True)
else:
    print(False)



