from config import BYBIT_API_KEY, BYBIT_API_SECRET, BYBIT_API_KEY_INTRA, BYBIT_API_SECRET_INTRA, BYBIT_API_KEY_INTRA2, BYBIT_API_SECRET_INTRA2, BYBIT_API_KEY_INTRA3, BYBIT_API_SECRET_INTRA3, BYBIT_API_KEY_CLASSIC, BYBIT_API_SECRET_CLASSIC, BYBIT_API_KEY_CLASSIC2, BYBIT_API_SECRET_CLASSIC2, BYBIT_API_KEY_CLASSIC3, BYBIT_API_SECRET_CLASSIC3, BYBIT_API_KEY_SWING, BYBIT_API_SECRET_SWING, BYBIT_API_KEY_SWING2, BYBIT_API_SECRET_SWING2, BYBIT_API_KEY_SWING3, BYBIT_API_SECRET_SWING3
from config import MAIN_ID, INTRA_ID, CLASSIC_ID, SWING_ID, INTRA2_ID, CLASSIC2_ID, SWING2_ID, INTRA3_ID, CLASSIC3_ID, SWING3_ID
from pybit.unified_trading import HTTP

session = HTTP(
    testnet=False,
    api_key=BYBIT_API_KEY,
    api_secret=BYBIT_API_SECRET,
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
MAIN_TRANSFERABLE = session.get_coin_balance(
    accountType="SPOT",
    coin="USDT",
    memberId=MAIN_ID
)['result']['balance']['transferBalance']

INTRA_TRANSFERABLE = sessionIntra.get_coin_balance(
    accountType="CONTRACT",
    coin="USDT",
    memberId=INTRA_ID,
    recv_window=10000
)['result']['balance']['transferBalance']

CLASSIC_TRANSFERABLE = sessionClassic.get_coin_balance(
    accountType="CONTRACT",
    coin="USDT",
    memberId=CLASSIC_ID
)['result']['balance']['transferBalance']
SWING_TRANSFERABLE = sessionSwing.get_coin_balance(
    accountType="CONTRACT",
    coin="USDT",
    memberId=SWING_ID
)['result']['balance']['transferBalance']
INTRA2_TRANSFERABLE = sessionIntra2.get_coin_balance(
    accountType="CONTRACT",
    coin="USDT",
    memberId=INTRA2_ID
)['result']['balance']['transferBalance']
CLASSIC2_TRANSFERABLE = sessionClassic2.get_coin_balance(
    accountType="CONTRACT",
    coin="USDT",
    memberId=CLASSIC2_ID
)['result']['balance']['transferBalance']
SWING2_TRANSFERABLE = sessionSwing2.get_coin_balance(
    accountType="CONTRACT",
    coin="USDT",
    memberId=SWING2_ID
)['result']['balance']['transferBalance']
INTRA3_TRANSFERABLE = sessionIntra3.get_coin_balance(
    accountType="CONTRACT",
    coin="USDT",
    memberId=INTRA3_ID
)['result']['balance']['transferBalance']
CLASSIC3_TRANSFERABLE = sessionClassic3.get_coin_balance(
    accountType="CONTRACT",
    coin="USDT",
    memberId=CLASSIC3_ID
)['result']['balance']['transferBalance']
SWING3_TRANSFERABLE = sessionSwing3.get_coin_balance(
    accountType="CONTRACT",
    coin="USDT",
    memberId=SWING3_ID
)['result']['balance']['transferBalance']

print("Transferable funds on :\n ",
      "MAIN ", MAIN_TRANSFERABLE,"\n",
      "INTRA ", INTRA_TRANSFERABLE,"\n",
      "CLASSIC ", CLASSIC_TRANSFERABLE,"\n",
      "SWING ", SWING_TRANSFERABLE,"\n",
      "INTRA2 ", INTRA2_TRANSFERABLE,"\n",
      "CLASSIC2 ", CLASSIC2_TRANSFERABLE,"\n",
      "SWING2 ", SWING2_TRANSFERABLE,"\n",
      "INTRA3 ",INTRA3_TRANSFERABLE,"\n",
      "CLASSIC3 ",CLASSIC3_TRANSFERABLE,"\n",
      "SWING3 ", SWING3_TRANSFERABLE,"\n")