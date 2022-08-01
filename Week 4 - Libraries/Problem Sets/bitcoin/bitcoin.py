import requests 
import sys 

if len(sys.argv) == 2: 
    try: 
        num = float(sys.argv[1])
    except: 
        sys.exit("Command-line argument is not a number")
else: 
    sys.exit("Missing command-line argument")

try: 
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    rate = r.json() 
    price = rate['bpi']['USD']['rate_float']
    print(f"${price * num:,.4f}")
except requests.RequestException: 
    sys.exit("RequestException")