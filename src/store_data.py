import pandas as pd
import os

def save_data(df):
    file_path = "data/crypto_prices.csv"

    file_exists = os.path.isfile(file_path)

    df.to_csv(
        file_path,
        mode='a',
        index=False,
        header=not file_exists   # ✅ write header only once
    )
