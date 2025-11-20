# Binance Testnet Bot Demo

A simplified trading bot for Binance Futures Testnet built using Python and Streamlit.
It allows users to connect to their Binance Testnet account, view balances, place market and OCO orders, and logs all actions.

# Features

## Connect/Disconnect Binance Testnet account using API key & Secret key

<p align="center">
<img width="600" alt="Screenshot (944)" src="https://github.com/user-attachments/assets/7e88e9e4-d25a-4237-9304-6899e21a5eff" />
</p>


## Display current USDT futures balance in tabular form

<p align="center">
  <img width="600" alt="Screenshot (945)" src="https://github.com/user-attachments/assets/3caeec62-14aa-4c7a-ac60-01f48ec1c0a9" />
</p>


## Place Market Orders (BUY/SELL)

<p align="center">
<img width="600" alt="Screenshot (946)" src="https://github.com/user-attachments/assets/b313e2ed-ba7f-45b3-a197-f9f968f6bdef" />
</p>


## Place OCO Orders (Take Profit + Stop Loss)

<p align="center">
<img width="600" alt="Screenshot (943)" src="https://github.com/user-attachments/assets/8ed65b6a-2b45-46b2-83ce-f32f8213f96e" />
</p>


## Logs all actions including login, orders, OCO orders, and logout:

<p align="center">
<img width="600" alt="image" src="https://github.com/user-attachments/assets/a278bcac-8ba9-44bf-a4eb-79a5bf565370" />
</p>


# Libraries Used

- streamlit – for UI/dashboard

- python-binance – official Python SDK for Binance API

- pandas – for displaying balances in table format

- logging – for maintaining logs of all actions

Install dependencies via pip:

`pip install streamlit python-binance pandas`

# How to Run

- Clone the repository or copy the code locally.

- Ensure you have Python 3.10+ installed.

- Open terminal in the project folder.

- Run the app with:
`streamlit run main.py`


# After running
- The app will open in your browser.

- Login: Enter your Binance Testnet API Key and Secret Key.

- Dashboard: After connecting, you can:

  - View your USDT balance on Binance Futures Testnet.

  - Place Market Orders.

  - Place OCO Orders (Take Profit + Stop Loss emulated).

- Logout: Disconnect your session when done.

# Notes

- The bot uses Binance Futures Testnet only – no real funds are involved.

- OCO orders are emulated by placing Take Profit and Stop Loss orders simultaneously.

- All actions (login, orders, errors) are logged in bot.log for tracking and debugging.
