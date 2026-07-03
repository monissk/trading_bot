from decimal import Decimal


VALID_SIDES = ["BUY", "SELL"]
VALID_ORDER_TYPES = ["MARKET", "LIMIT"]


def validate_symbol(symbol):
    """
    Validate trading symbol.
    """

    if not symbol:
        raise ValueError("Symbol cannot be empty.")

    symbol = symbol.upper()

    if not symbol.endswith("USDT"):
        raise ValueError("Only USDT-M Futures symbols are supported (e.g. BTCUSDT).")

    return symbol


def validate_side(side):
    """
    Validate BUY / SELL.
    """

    side = side.upper()

    if side not in VALID_SIDES:
        raise ValueError("Side must be BUY or SELL.")

    return side


def validate_order_type(order_type):
    """
    Validate MARKET / LIMIT.
    """

    order_type = order_type.upper()

    if order_type not in VALID_ORDER_TYPES:
        raise ValueError("Order type must be MARKET or LIMIT.")

    return order_type


def validate_quantity(quantity):
    """
    Validate order quantity.
    """

    try:
        quantity = Decimal(str(quantity))

    except Exception:
        raise ValueError("Quantity must be a valid number.")

    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero.")

    return float(quantity)


def validate_price(price, order_type):
    """
    Validate price for LIMIT order.
    """

    if order_type.upper() == "MARKET":
        return None

    if price is None:
        raise ValueError("Price is required for LIMIT orders.")

    try:
        price = Decimal(str(price))

    except Exception:
        raise ValueError("Price must be a valid number.")

    if price <= 0:
        raise ValueError("Price must be greater than zero.")

    return float(price)


def validate_inputs(symbol, side, order_type, quantity, price=None):
    """
    Validate all inputs together.
    """

    symbol = validate_symbol(symbol)
    side = validate_side(side)
    order_type = validate_order_type(order_type)
    quantity = validate_quantity(quantity)
    price = validate_price(price, order_type)

    return {
        "symbol": symbol,
        "side": side,
        "order_type": order_type,
        "quantity": quantity,
        "price": price,
    }