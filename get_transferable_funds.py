from config import BYBIT_API_KEY, BYBIT_API_SECRET
from config import MAIN_ID,INTRA_ID,CLASSIC_ID,SWING_ID,INTRA2_ID,CLASSIC2_ID,SWING2_ID,INTRA3_ID,CLASSIC3_ID,SWING3_ID
from pybit.unified_trading import HTTP

session = HTTP(
    testnet=False,
    api_key=BYBIT_API_KEY,
    api_secret=BYBIT_API_SECRET,
)

MAIN_TRANSFERABLE = session.get_coin_balance(
    accountType="SPOT",
    coin="USDT",
    memberId=MAIN_ID
)
INTRA_TRANSFERABLE = session.get_coin_balance(
    accountType="CONTRACT",
    coin="USDT",
    memberId=INTRA_ID
)
CLASSIC_TRANSFERABLE = session.get_coin_balance(
    accountType="CONTRACT",
    coin="USDT",
    memberId=CLASSIC_ID
)
SWING_TRANSFERABLE = session.get_coin_balance(
    accountType="CONTRACT",
    coin="USDT",
    memberId=SWING_ID
)
INTRA2_TRANSFERABLE = session.get_coin_balance(
    accountType="CONTRACT",
    coin="USDT",
    memberId=INTRA2_ID
)
CLASSIC2_TRANSFERABLE = session.get_coin_balance(
    accountType="CONTRACT",
    coin="USDT",
    memberId=CLASSIC2_ID
)
SWING2_TRANSFERABLE = session.get_coin_balance(
    accountType="CONTRACT",
    coin="USDT",
    memberId=SWING2_ID
)
INTRA3_TRANSFERABLE = session.get_coin_balance(
    accountType="CONTRACT",
    coin="USDT",
    memberId=INTRA3_ID
)
CLASSIC3_TRANSFERABLE = session.get_coin_balance(
    accountType="CONTRACT",
    coin="USDT",
    memberId=CLASSIC3_ID
)
SWING3_TRANSFERABLE = session.get_coin_balance(
    accountType="CONTRACT",
    coin="USDT",
    memberId=SWING3_ID
)