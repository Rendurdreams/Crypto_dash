import requests
import mysql.connector

def fetch_crypto_data(api_key, crypto_ids):
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
    parameters = {'id': ','.join(crypto_ids)}  # Join ids into a single string
    headers = {'X-CMC_PRO_API_KEY': api_key}
    response = requests.get(url, headers=headers, params=parameters)
    return response.json()

def insert_data_into_db(data):
    conn = mysql.connector.connect(
        host='localhost',
        user='rendur',  # Replace with your username
        password='[vt%WMQX-$x2SR/',  # Replace with your password, if set
        database='crypto_data'
    )
    cursor = conn.cursor()

    # Assuming 'data' is a dictionary with your cryptocurrency data
       # Assuming 'data' is a dictionary with your cryptocurrency data
    insert_query = (
        "INSERT INTO cryptocurrencies (id, name, symbol, price, market_cap, volume_24h, percent_change_1h, percent_change_24h, last_updated) "
        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) "
        "ON DUPLICATE KEY UPDATE "
        "name = VALUES(name), symbol = VALUES(symbol), price = VALUES(price), market_cap = VALUES(market_cap), "
        "volume_24h = VALUES(volume_24h), percent_change_1h = VALUES(percent_change_1h), percent_change_24h = VALUES(percent_change_24h), last_updated = VALUES(last_updated)"
    )
    cursor.execute(insert_query, (
        data['id'], data['name'], data['symbol'], data['price'], data['market_cap'], data['volume_24h'], data['percent_change_1h'], data['percent_change_24h'], data['last_updated']
    ))

    conn.commit()
    cursor.close()
    conn.close()

def main():
    api_key = '972f6a08-81de-4288-866c-3d0dca592465'  # Replace with your CoinMarketCap API key
    crypto_ids = ['52', '3155','4642','2634','512','5899','3077','3816','9308','10047','3773','12749','5690']  # replace with desired crypto IDs
    data = fetch_crypto_data(api_key, crypto_ids)

    if data['status']['error_code'] == 0:
        for crypto_id in crypto_ids:
            if str(crypto_id) in data['data']:
                coin = data['data'][str(crypto_id)]
                name = coin['name']
                symbol = coin['symbol']
                price = coin['quote']['USD']['price']
                market_cap = coin['quote']['USD']['market_cap']
                volume_24h = coin['quote']['USD']['volume_24h']
                percent_change_1h = coin['quote']['USD']['percent_change_1h']
                percent_change_24h = coin['quote']['USD']['percent_change_24h']
                last_updated = coin['last_updated']

                # Inserting data into the database
                insert_data_into_db({
                    'id': crypto_id,
                    'name': name,
                    'symbol': symbol,
                    'price': price,
                    'market_cap': market_cap,
                    'volume_24h': volume_24h,
                    'percent_change_1h': percent_change_1h,
                    'percent_change_24h': percent_change_24h,
                    'last_updated': last_updated
                })
    else:
        print("Error:", data['status']['error_message'])

if __name__ == "__main__":
    main()