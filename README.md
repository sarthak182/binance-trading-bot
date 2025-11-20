## Binance Testnet Bot Demo

A simplified trading bot for Binance Futures Testnet built using Python and Streamlit.
It allows users to connect to their Binance Testnet account, view balances, place market and OCO orders, and logs all actions.

# Features

Connect/Disconnect Binance Testnet account using API key & Secret key

Display current USDT futures balance in tabular form

Place Market Orders (BUY/SELL)

Place OCO Orders (Take Profit + Stop Loss)

Logs all actions including login, orders, OCO orders, and logout

<img width="1920" height="1080" alt="Screenshot (943)" src="https://github.com/user-attachments/assets/b313e2ed-ba7f-45b3-a197-f9f968f6bdef" />
<img width="1920" height="1080" alt="Screenshot (944)" src="https://github.com/user-attachments/assets/b313e2ed-ba7f-45b3-a197-f9f968f6bdef" />
<img width="1920" height="1080" alt="Screenshot (945)" src="https://github.com/user-attachments/assets/b313e2ed-ba7f-45b3-a197-f9f968f6bdef" />
<img width="1920" height="1080" alt="Screenshot (946)" src="https://github.com/user-attachments/assets/b313e2ed-ba7f-45b3-a197-f9f968f6bdef" />
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
