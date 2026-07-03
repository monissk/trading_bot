# Binance Futures Testnet Trading Bot

A Python-based command-line trading bot for **Binance USDT-M Futures Testnet**.

This project was developed as part of the Python Developer Internship assignment for Primetrade.ai.

---

## Features

- Place **MARKET** orders
- Place **LIMIT** orders
- Supports both **BUY** and **SELL**
- Input validation
- Logging of API requests, responses, and errors
- Exception handling
- Modular and reusable project structure

---

## Project Structure

```
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── logs/
│   └── trading_bot.log
│
├── .env
├── cli.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Requirements

- Python 3.10+
- Binance Futures Testnet Account
- Binance API Key
- Binance Secret Key

---

## Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/binance-futures-trading-bot.git
```

or

Download the ZIP file and extract it.

---

### Create Virtual Environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure API Keys

Create a file named `.env`

```
BINANCE_API_KEY=YOUR_API_KEY
BINANCE_SECRET_KEY=YOUR_SECRET_KEY
```

Generate API Keys from

https://testnet.binancefuture.com

---

## Usage

### MARKET Order

```bash
python cli.py \
--symbol BTCUSDT \
--side BUY \
--type MARKET \
--quantity 0.001
```

---

### LIMIT Order

```bash
python cli.py \
--symbol BTCUSDT \
--side SELL \
--type LIMIT \
--quantity 0.001 \
--price 120000
```

---

## Example Output

```
========== ORDER REQUEST ==========

Symbol      : BTCUSDT
Side        : BUY
Order Type  : MARKET
Quantity    : 0.001

===================================

========== ORDER RESPONSE ==========

Order ID      : 123456789
Status        : FILLED
Executed Qty  : 0.001
Average Price : 108420

===================================
```

---

## Logging

Logs are stored inside

```
logs/trading_bot.log
```

Logs include

- API Requests
- API Responses
- Validation Errors
- Network Errors
- Binance API Errors

---

## Assumptions

- Only USDT-M Futures are supported.
- Supported order types:
  - MARKET
  - LIMIT
- Supported sides:
  - BUY
  - SELL
- LIMIT orders require a price.
- MARKET orders do not require a price.

---

## Technologies Used

- Python 3
- python-binance
- argparse
- logging
- python-dotenv

---

## Future Improvements

- Stop-Limit Orders
- OCO Orders
- Interactive CLI
- Rich Console UI
- Order History
- Position Monitoring

---

## Author

Monis

B.Tech Computer Science and Business Systems

Bharati Vidyapeeth College of Engineering, Pune