from binance.enums import *
from binance.exceptions import BinanceAPIException, BinanceOrderException

from bot.client import get_client
from bot.logging_config import logger





def _print_order_summary(order):
    """
    Print important order details.
    """

    print("\n========== ORDER RESPONSE ==========")
    print(f"Order ID      : {order.get('orderId')}")
    print(f"Status        : {order.get('status')}")
    print(f"Symbol        : {order.get('symbol')}")
    print(f"Side          : {order.get('side')}")
    print(f"Type          : {order.get('type')}")
    print(f"Executed Qty  : {order.get('executedQty')}")

    if "avgPrice" in order:
        print(f"Average Price : {order.get('avgPrice')}")

    print("====================================\n")


def place_market_order(symbol, side, quantity):
    client = get_client()
    """
    Place a Futures MARKET order.
    """

    try:

        logger.info(
            f"MARKET ORDER | Symbol={symbol} Side={side} Qty={quantity}"
        )

        order = client.futures_create_order(
            symbol=symbol.upper(),
            side=side.upper(),
            type="MARKET",
            quantity=quantity
        )

        logger.info(f"SUCCESS : {order}")

        _print_order_summary(order)

        return order

    except BinanceAPIException as e:

        logger.error(f"Binance API Error : {e}")

        print(f"\nAPI Error : {e.message}")

    except BinanceOrderException as e:

        logger.error(f"Order Error : {e}")

        print(f"\nOrder Error : {e}")

    except Exception as e:

        logger.exception("Unexpected Error")

        print(f"\nUnexpected Error : {e}")


def place_limit_order(symbol, side, quantity, price):
    client = get_client()
    """
    Place a Futures LIMIT order.
    """

    try:

        logger.info(
            f"LIMIT ORDER | Symbol={symbol} "
            f"Side={side} Qty={quantity} Price={price}"
        )

        order = client.futures_create_order(
            symbol=symbol.upper(),
            side=side.upper(),
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )

        logger.info(f"SUCCESS : {order}")

        _print_order_summary(order)

        return order

    except BinanceAPIException as e:

        logger.error(f"Binance API Error : {e}")

        print(f"\nAPI Error : {e.message}")

    except BinanceOrderException as e:

        logger.error(f"Order Error : {e}")

        print(f"\nOrder Error : {e}")

    except Exception as e:

        logger.exception("Unexpected Error")

        print(f"\nUnexpected Error : {e}")