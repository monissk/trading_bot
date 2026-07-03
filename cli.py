"""
cli.py

Command Line Interface for Binance Futures Testnet Trading Bot.
"""

import argparse
import sys

from bot.orders import place_market_order, place_limit_order
from bot.validators import validate_inputs
from bot.logging_config import logger


def print_summary(data):
    """
    Print order request summary.
    """
    print("\n========== ORDER REQUEST ==========")
    print(f"Symbol      : {data['symbol']}")
    print(f"Side        : {data['side']}")
    print(f"Order Type  : {data['order_type']}")
    print(f"Quantity    : {data['quantity']}")

    if data["order_type"] == "LIMIT":
        print(f"Price       : {data['price']}")

    print("===================================\n")


def main():

    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument(
        "--symbol",
        required=True,
        help="Trading symbol (e.g. BTCUSDT)"
    )

    parser.add_argument(
        "--side",
        required=True,
        help="BUY or SELL"
    )

    parser.add_argument(
        "--type",
        required=True,
        help="MARKET or LIMIT"
    )

    parser.add_argument(
        "--quantity",
        required=True,
        type=float,
        help="Order quantity"
    )

    parser.add_argument(
        "--price",
        type=float,
        help="Price (Required for LIMIT orders)"
    )

    args = parser.parse_args()

    try:

        data = validate_inputs(
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price
        )

        print_summary(data)

        logger.info("Validated user input successfully.")

        if data["order_type"] == "MARKET":

            place_market_order(
                symbol=data["symbol"],
                side=data["side"],
                quantity=data["quantity"]
            )

        else:

            place_limit_order(
                symbol=data["symbol"],
                side=data["side"],
                quantity=data["quantity"],
                price=data["price"]
            )

        print("\n✅ Order submitted successfully.")

    except ValueError as e:

        logger.error(f"Validation Error: {e}")
        print(f"\n❌ Validation Error: {e}")
        sys.exit(1)

    except Exception as e:

        logger.exception("Unexpected Error")
        print(f"\n❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()