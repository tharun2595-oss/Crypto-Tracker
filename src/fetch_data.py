import requests
import pandas as pd
from datetime import datetime
import time
from store_data import save_data

url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"

while True:
    try:
        response = requests.get(url)
        data = response.json()

        if 'bitcoin' in data and 'ethereum' in data:
            btc_price = data['bitcoin']['usd']
            eth_price = data['ethereum']['usd']

            df = pd.DataFrame([{
                "timestamp": datetime.now(),
                "bitcoin": btc_price,
                "ethereum": eth_price
            }])

            save_data(df)

            print("✅ Data fetched:", df)

        else:
            print("⚠️ API issue:", data)

    except Exception as e:
        print("❌ Error:", e)

    time.sleep(60)
