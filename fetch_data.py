import requests

def fetch_crypto_data(api_key, crypto_id):
    url = f"https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
    parameters = {'id': crypto_id}
    headers = {'X-CMC_PRO_API_KEY': api_key}
    response = requests.get(url, headers=headers, params=parameters)
    return response.json()

def main():
    api_key = '972f6a08-81de-4288-866c-3d0dca592465'  # Replace with your CoinMarketCap API key
    crypto_id = '52'  # Example for Bitcoin; replace with desired crypto ID
    data = fetch_crypto_data(api_key, crypto_id)
    print(data)  # For testing, print out the data

if __name__ == "__main__":
    main()