import os
from dotenv import load_dotenv
from binance.client import Client
from binance.exceptions import BinanceAPIException

# Load environment variables
load_dotenv()

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_SECRET_KEY")


def get_client():
    """
    Create and return a Binance Futures Testnet client.
    """

    if not API_KEY or not API_SECRET:
        raise ValueError(
            "API Key or Secret Key not found. Please check your .env file."
        )

    try:
        client = Client(API_KEY, API_SECRET, testnet=True)

        # Test API connection
        client.futures_account_balance()

        return client

    except BinanceAPIException as e:
        raise Exception(f"Binance API Error: {e.message}")

    except Exception as e:
        raise Exception(f"Unable to connect to Binance Futures Testnet: {e}")
