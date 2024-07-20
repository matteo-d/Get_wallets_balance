# Get Wallets Balance
from config import BYBIT_API_KEY, BYBIT_API_SECRET, BYBIT_API_KEY_INTRA, BYBIT_API_SECRET_INTRA, BYBIT_API_KEY_INTRA2, BYBIT_API_SECRET_INTRA2, BYBIT_API_KEY_INTRA3, BYBIT_API_SECRET_INTRA3, BYBIT_API_KEY_CLASSIC, BYBIT_API_SECRET_CLASSIC, BYBIT_API_KEY_CLASSIC2, BYBIT_API_SECRET_CLASSIC2, BYBIT_API_KEY_CLASSIC3, BYBIT_API_SECRET_CLASSIC3, BYBIT_API_KEY_SWING, BYBIT_API_SECRET_SWING, BYBIT_API_KEY_SWING2, BYBIT_API_SECRET_SWING2, BYBIT_API_KEY_SWING3, BYBIT_API_SECRET_SWING3
from config import BANK
from pybit.unified_trading import HTTP
import time

session = HTTP(
    testnet=False,
    api_key=BYBIT_API_KEY,
    api_secret=BYBIT_API_SECRET
)
sessionIntra = HTTP(
    testnet=False,
    api_key=BYBIT_API_KEY_INTRA,
    api_secret=BYBIT_API_SECRET_INTRA
)
sessionIntra2 = HTTP(
    testnet=False,
    api_key=BYBIT_API_KEY_INTRA2,
    api_secret=BYBIT_API_SECRET_INTRA2
)
sessionIntra3 = HTTP(
    testnet=False,
    api_key=BYBIT_API_KEY_INTRA3,
    api_secret=BYBIT_API_SECRET_INTRA3
)
sessionClassic = HTTP(
    testnet=False,
    api_key=BYBIT_API_KEY_CLASSIC,
    api_secret=BYBIT_API_SECRET_CLASSIC
)
sessionClassic2 = HTTP(
    testnet=False,
    api_key=BYBIT_API_KEY_CLASSIC2,
    api_secret=BYBIT_API_SECRET_CLASSIC2    
)
sessionClassic3 = HTTP(
    testnet=False,
    api_key=BYBIT_API_KEY_CLASSIC3,
    api_secret=BYBIT_API_SECRET_CLASSIC3    
)
sessionSwing = HTTP(
    testnet=False,
    api_key=BYBIT_API_KEY_SWING,
    api_secret=BYBIT_API_SECRET_SWING    
)
sessionSwing2 = HTTP(
    testnet=False,
    api_key=BYBIT_API_KEY_SWING2,
    api_secret=BYBIT_API_SECRET_SWING2    
)
sessionSwing3 = HTTP(
    testnet=False,
    api_key=BYBIT_API_KEY_SWING3,
    api_secret=BYBIT_API_SECRET_SWING3    
)

print(session.get_positions(
    category="inverse",
    symbol="BTCUSD",
))