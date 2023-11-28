import requests

def fetch_crypto_data(api_key, crypto_ids):
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
    parameters = {'id': ','.join(crypto_ids)}  # Join ids into a single string
    headers = {'X-CMC_PRO_API_KEY': api_key}
    response = requests.get(url, headers=headers, params=parameters)
    return response.json()

def main():
    api_key = '972f6a08-81de-4288-866c-3d0dca592465'  # Replace with your CoinMarketCap API key
    crypto_ids = ['52', '3816', '28498', '4166', '12749', '5690']  # replace with desired crypto IDs
    data = fetch_crypto_data(api_key, crypto_ids)

    if data['status']['error_code'] == 0:
        for crypto_id in crypto_ids:
            if str(crypto_id) in data['data']:
                coin = data['data'][str(crypto_id)]
                name = coin['name']
                symbol = coin['symbol']
                price = coin['quote']['USD']['price']
                market_cap = coin['quote']['USD']['market_cap']

                # Printing extracted information
                print(f"Name: {name}")
                print(f"Symbol: {symbol}")
                print(f"Price: ${price:.2f}")
                print(f"Market Cap: ${market_cap:.2f}")
            else:
                print(f"No data found for ID {crypto_id}")
    else:
        print("Error:", data['status']['error_message'])

if __name__ == "__main__":
    main()