import streamlit as st
from binance import Client
import pandas as pd
from binance.enums import *
from binance.exceptions import BinanceAPIException
from log import logger


def place_futures_order(api_key, api_secret, symbol, side, quantity):
    """Places a market futures order on Binance Testnet.
    Returns: {success: bool, message: str, data: dict or None}
    """

    logger.info(f"Order request → Symbol={symbol}, Side={side}, Qty={quantity}")

    client = Client(api_key, api_secret, testnet=True)

    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type=ORDER_TYPE_MARKET,
            quantity=quantity
        )

        logger.info(f"Order successful → {order}")

        return {
            "success": True,
            "message": "Order placed successfully",
            "data": order
        }

    except BinanceAPIException as e:
        logger.error(f"Binance API Error during order → {e.message}")

        return {
            "success": False,
            "message": f"Binance API Error: {e.message}",
            "data": None
        }

    except Exception as e:
        logger.error(f"Unexpected Error during order → {str(e)}")

        return {
            "success": False,
            "message": f"Unexpected error: {str(e)}",
            "data": None
        }

def place_oco_futures_order(client, symbol, side, take_profit_price, stop_loss_price):
    try:
        opposite_side = SIDE_SELL if side == SIDE_BUY else SIDE_BUY

        # TAKE PROFIT ORDER
        tp_order = client.futures_create_order(
            symbol=symbol,
            side=opposite_side,
            type="TAKE_PROFIT_MARKET",
            stopPrice=str(take_profit_price),
            closePosition=True
        )

        # STOP LOSS ORDER
        sl_order = client.futures_create_order(
            symbol=symbol,
            side=opposite_side,
            type="STOP_MARKET",
            stopPrice=str(stop_loss_price),
            closePosition=True
        )

        return {
            "success": True,
            "message": "OCO (TP + SL) placed successfully!",
            "data": {"tp_order": tp_order, "sl_order": sl_order}
        }

    except Exception as e:
        return {
            "success": False,
            "message": f"OCO order failed: {e}"
        }
st.title("Binance Testnet Bot Demo")

if "connected" not in st.session_state:
    st.session_state.connected = False
if "client" not in st.session_state:
    st.session_state.client = None


# -------------------------
# LOGIN PAGE
# -------------------------
def login_page():
    st.title("🔐 Connect to Binance Futures")

    api_key = st.text_input("Enter API Key", type="password")
    api_secret = st.text_input("Enter Secret Key", type="password")

    if st.button("Connect"):
        if not api_key or not api_secret:
            st.error("Please enter both API key and Secret key.")
            return

        logger.info(f"Login attempt with API key prefix: {api_key[:4]}***")

        try:
            client = Client(api_key, api_secret, testnet=True)
            balance = client.futures_account_balance()
            usdt_balance = next((b for b in balance if b["asset"] == "USDT"), None)

            st.session_state.connected = True
            st.session_state.client = client

            logger.info("Login successful")
            logger.info(f"Balance fetched: {usdt_balance}")

            st.success("Login successful! Redirecting...")

            st.rerun()  # → MOVE TO NEXT PAGE

        except BinanceAPIException as e:
            logger.error(f"Binance API error: {e}")
            st.error(f"Binance API error: {e}")

        except Exception as e:
            logger.error(f"Unexpected login error: {e}")
            st.error(f"Error: {e}")


# -------------------------
# DASHBOARD PAGE
# -------------------------

def dashboard():
    st.title("📊 Trading Dashboard")

    st.subheader("Account Balance")

    logger.info("Fetching balance on dashboard")

    balance = st.session_state.client.futures_account_balance()
    usdt_balance = next((b for b in balance if b["asset"] == "USDT"), None)

    df = pd.DataFrame([usdt_balance])
    st.table(df)

    st.subheader("Place Order")

    symbol = st.selectbox("Symbol", ["BTCUSDT", "ETHUSDT"])
    side = st.selectbox("Side (Entry)", ["BUY", "SELL"])
    quantity = st.number_input("Quantity", min_value=0.001, step=0.001)

    # FOR MARKET ORDER
    if st.button("Place Market Order"):
        logger.info(f"Market order clicked: {symbol}, {side}, qty={quantity}")

        try:
            order = st.session_state.client.futures_create_order(
                symbol=symbol,
                side=SIDE_BUY if side == "BUY" else SIDE_SELL,
                type="MARKET",
                quantity=quantity
            )

            st.success("Market Order Placed!")
            st.json(order)

            logger.info(f"Market order placed → {order}")

        except Exception as e:
            st.error(f"Failed: {e}")
            logger.error(f"Order error → {e}")

    # FOR OCO ORDER
    st.subheader("OCO Order (Emulated)")

    take_profit_price = st.number_input(
        "Take Profit Price",
        min_value=0.0,
        step=0.1,
        format="%.4f"
    )

    stop_loss_price = st.number_input(
        "Stop Loss Price",
        min_value=0.0,
        step=0.1,
        format="%.4f"
    )

    if st.button("Place OCO Order"):
        logger.info(
            f"OCO request → {symbol}, entry={side}, TP={take_profit_price}, SL={stop_loss_price}"
        )

        if take_profit_price <= 0 or stop_loss_price <= 0:
            st.error("Both TP and SL must be greater than 0!")
        else:
            result = place_oco_futures_order(
                st.session_state.client,
                symbol,
                SIDE_BUY if side == "BUY" else SIDE_SELL,
                take_profit_price,
                stop_loss_price
            )

            if result["success"]:
                st.success(result["message"])
                st.json(result["data"])
            else:
                st.error(result["message"])


    # LOGOUT FUNCTION
    if st.button("Logout"):
        st.session_state.connected = False
        st.session_state.client = None
        logger.info("User logged out")
        st.rerun()



# -------------------------
# ROUTER
# -------------------------
if not st.session_state.connected:
    login_page()      # show login
else:
    dashboard()       # show dashboard