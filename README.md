## Binance Testnet Bot Demo

A simplified trading bot for Binance Futures Testnet built using Python and Streamlit.
It allows users to connect to their Binance Testnet account, view balances, place market and OCO orders, and logs all actions.

# Features

Connect/Disconnect Binance Testnet account using API key & Secret key
<img width="1920" height="1080" alt="Screenshot (944)" src="https://github.com/user-attachments/assets/7e88e9e4-d25a-4237-9304-6899e21a5eff" />

Display current USDT futures balance in tabular form
<img width="1920" height="1080" alt="Screenshot (945)" src="https://github.com/user-attachments/assets/3caeec62-14aa-4c7a-ac60-01f48ec1c0a9" />

Place Market Orders (BUY/SELL)
<img width="1920" height="1080" alt="Screenshot (946)" src="https://github.com/user-attachments/assets/b313e2ed-ba7f-45b3-a197-f9f968f6bdef" />

Place OCO Orders (Take Profit + Stop Loss)
<img width="1920" height="1010" alt="Screenshot (943)" src="https://github.com/user-attachments/assets/8ed65b6a-2b45-46b2-83ce-f32f8213f96e" />

Logs all actions including login, orders, OCO orders, and logout

# Libraries Used

streamlit – for UI/dashboard

python-binance – official Python SDK for Binance API

pandas – for displaying balances in table format

logging – for maintaining logs of all actions

Install dependencies via pip:

`pip install streamlit python-binance pandas`

# How to Run

Clone the repository or copy the code locally.

Ensure you have Python 3.10+ installed.

Open terminal in the project folder.

Run the app:

`streamlit run main.py`


The app opens in a browser window:

Enter your Binance Testnet API key and Secret key

Connect to view balances and access the dashboard

Place Market Orders or OCO Orders

Logout when done

Notes

The bot uses Binance Futures Testnet only, no real money is involved.

OCO orders are emulated by placing a Take Profit and Stop Loss order simultaneously.

Logs are stored in bot.log for all actions.
