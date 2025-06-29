import requests
import sys




try:
    if len(sys.argv) == 1:
        sys.exit("Missing command-line argument")

    elif len(sys.argv) == 2:

        n = sys.argv[1]
        n = float(n)
        x = n*10
        x = int(x)
        x = str(x)
        
        if x.isnumeric() == False:
            sys.exit("Command-line argument is not a number")

        elif float(n)>=1:

            r = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=45f484cb684b22ab53de18ea9d60466f5164072d6243f1e260961568a2b42264")

            data = r.json()

            price_btc = data["data"]["priceUsd"]
            amount = float(price_btc)*float(n)

            print(f"${amount:,.4f}")






except requests.RequestException:
    sys.exit("asd")
