from pyfiglet import Figlet
import sys
value = input("Input : ")

figlet = Figlet()

s = figlet.getFonts()
if len(sys.argv) > 3:
    print("Invalid usage")

elif len(sys.argv) == 1: 
    print(figlet.renderText(value))
else : 
    if sys.argv[1] in ["-f", "--font"]:
        if sys.argv[2] in s:
            figlet.setFont(font=sys.argv[2])
            print(figlet.renderText(value))
        else :
            print("Invalid usage")
    else :  
        sys.exit("Invalid usage")
        
    
    
    