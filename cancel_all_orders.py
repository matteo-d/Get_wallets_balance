from config import BYBIT_API_KEY, BYBIT_API_SECRET
from pybit.unified_trading import HTTP

# CREATE SESSION TO USE USE API V5
session = HTTP(
    testnet=False,
    api_key=BYBIT_API_KEY,
    api_secret=BYBIT_API_SECRET,
)

print(session.cancel_all_orders(
    category="linear",
    settleCoin="USDT",
))