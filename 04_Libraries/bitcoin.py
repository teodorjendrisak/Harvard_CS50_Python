import requests
import sys
import json


def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    try:
        response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=d121a3edc9d48cda7011f2cffed95d5697f5339c02be6ccf0454e5eb92e107a1")
        response.raise_for_status
    except requests.RequestException:
        sys.exit("Error fetching data from API")

    o = response.json()
    price = float(o["data"]["priceUsd"])
    print(f"{price * n:,.4f}")


if __name__ == "__main__":
    main()