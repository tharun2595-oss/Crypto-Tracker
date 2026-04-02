import pandas as pd

df = pd.read_csv("data/crypto_prices.csv")

latest = df.iloc[-1]

btc = latest['bitcoin']
eth = latest['ethereum']

if btc > 70000:
    print(" Bitcoin crossed 70K!")

if eth  > 4000:
    print(" Ethereum crossed 4K!")
