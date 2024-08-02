import re
import sys 

def main():
    print(validate(input("IP addresse : ").strip()))



def validate(ip):
    if matches := re.search(r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$", ip):
        numbers_in_ip = ip.split('.')
        for number in numbers_in_ip:
            if int(number) > 255 or int(number) < 0:
                return False
            else :
                continue
        return True
    else : 
        return False


if __name__=="__main__":
    main()