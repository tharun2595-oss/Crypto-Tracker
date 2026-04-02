# Real-Time Crypto Price Tracker

##  Project Overview

This project is a real-time cryptocurrency tracking system that fetches live prices of Bitcoin and Ethereum using a public API and stores them for analysis.

It also includes a dashboard and alert system to monitor price movements.

---

##  Features

*  Fetches real-time crypto prices using API
*  Stores data continuously in CSV
*  Analyzes historical trends
*  Alerts when price crosses threshold
*  Interactive dashboard using Streamlit

---

##  Tech Stack

* Python
* Pandas
* Requests (API handling)
* Streamlit (Dashboard)

---

##  Project Structure

crypto-tracker/
│
├── data/
│   └── crypto_prices.csv
│
├── src/
│   ├── fetch_data.py
│   ├── store_data.py
│   ├── analyze.py
│   ├── alert.py
│
├── dashboard/
│   └── app.py
│
├── requirements.txt
└── README.md

---

## ️ How to Run

### 1. Install dependencies

pip install -r requirements.txt

### 2. Start data collection

python src/fetch_data.py

### 3. Run analysis

python src/analyze.py

### 4. Run dashboard

streamlit run dashboard/app.py

---

##  Key Insights

* Tracks price trends over time
* Calculates average and maximum prices
* Helps monitor market movements

---

##  Alert System

* Alerts triggered when:

  * Bitcoin > 70,000 USD
  * Ethereum > 4,000 USD

---

##  Future Improvements

* Email/Telegram alerts
* Database integration (SQLite/PostgreSQL)
* Support for multiple cryptocurrencies
* Deployment of dashboard

---

## ‍ Author

Tharun Reddy

