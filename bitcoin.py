import requests
import json 
import sys 

r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

data = r.json()

#print(json.dumps(r.json(), indent=2))

btc = float(data['bpi']["USD"]["rate_float"])

while True:
    try:
        amount = float(sys.argv[1]) * btc
        print(f'${amount:,.4f}')
        sys.exit()
    except (TypeError, ValueError):
        sys.exit("Command-line argument is not a number")
    except IndexError:
        sys.exit('Missing command-line argument')
        







