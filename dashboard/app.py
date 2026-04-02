import streamlit as st
import pandas as pd

df = pd.read_csv("data/crypto_prices.csv")

st.title(" Crypto Tracker Dashboard")

st.metric("Latest BTC", df['bitcoin'].iloc[-1])
st.metric("Latest ETH", df['ethereum'].iloc[-1])

st.line_chart(df[['bitcoin', 'ethereum']])
