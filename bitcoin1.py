import requests 
import json


r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

data = r.json()
print(data['time']['updated'])
print(data['bpi']['EUR']['rate_float'])

a = {'time': {'updated': 'Aug 2, 2024 23:15:53 UTC', 'updatedISO': '2024-08-02T23:15:53+00:00', 'updateduk': 'Aug 3, 2024 at 00:15 BST'}, 
'disclaimer': 'This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org', 'chartName': 'Bitcoin', 
'bpi': {'USD': 
    {'code': 'USD', 'symbol': '&#36;', 'rate': '61,851.579', 'description': 'United States Dollar', 'rate_float': 61851.5785}, 
    'GBP': {'code': 'GBP', 'symbol': '&pound;', 'rate': '48,306.083', 'description': 'British Pound Sterling', 'rate_float': 48306.0828}, 
    'EUR': {'code': 'EUR', 'symbol': '&euro;', 'rate': '56,638.047', 'description': 'Euro', 'rate_float': 56638.0471}}}

