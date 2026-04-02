import pandas as pd

df = pd.read_csv("data/crypto_prices.csv")

print("\nLatest Prices:\n", df.tail(1))

print("\nAverage Prices:\n", df[['bitcoin', 'ethereum']].mean())

print("\nMax Prices:\n", df[['bitcoin', 'ethereum']].max())
