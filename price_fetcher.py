import requests

def get_price_diff(token_symbol="SOL"):
    try:
        url = f"https://price.jup.ag/v4/price?ids={token_symbol}"
        response = requests.get(url)
        data = response.json()

        price = data['data'][token_symbol]['price']
        # Simulate price difference for testing
        diff = round(price * 0.03, 4)
        return {"diff": diff, "price": price}
    except Exception as e:
        print(f"[🚨] Error fetching price for {token_symbol}: {e}")
        return {"diff": 0.0, "price": 0.0}
