import logging
import os


def setup_logger():
    """
    Configure and return the application logger.
    """

    # Create logs directory if it doesn't exist
    os.makedirs("logs", exist_ok=True)

    logger = logging.getLogger("TradingBot")
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers
    if logger.hasHandlers():
        return logger

    # Log format
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    # File Handler
    file_handler = logging.FileHandler(
        "logs/trading_bot.log",
        encoding="utf-8"
    )
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)

    # Console Handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    # Add handlers
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


# Create logger instance
logger = setup_logger()