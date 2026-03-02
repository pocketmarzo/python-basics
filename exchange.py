import sys
import requests

def main():

    if len(sys.argv) != 3:
        sys.exit("Usage: python exchange.py [amount] [currency_code]")

    try:
        number = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    currency = sys.argv[2].upper()
    url = "https://open.er-api.com/v6/latest/USD"

    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    rate = data["rates"]

    try:

        if currency in rate:
            result = number * rate[currency]
            print(f"{number} USD = {result:.2f} {currency}")
        else:
            available = list(rate.keys())
            available = list(rate.keys())
            print(f"Error: Currency '{currency}' not found.")
            print("Available currencies (first 10):", ", ".join(available[:10]))
            sys.exit()
    
    except KeyError:
        sys.exit()
main()

