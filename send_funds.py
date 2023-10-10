# Script to send funds from futures to spot
from config import BYBIT_API_KEY, BYBIT_API_SECRET, BYBIT_API_KEY_INTRA, BYBIT_API_SECRET_INTRA, BYBIT_API_KEY_INTRA2, BYBIT_API_SECRET_INTRA2, BYBIT_API_KEY_INTRA3, BYBIT_API_SECRET_INTRA3, BYBIT_API_KEY_CLASSIC, BYBIT_API_SECRET_CLASSIC, BYBIT_API_KEY_CLASSIC2, BYBIT_API_SECRET_CLASSIC2,BYBIT_API_KEY_CLASSIC3, BYBIT_API_SECRET_CLASSIC3, BYBIT_API_KEY_SWING, BYBIT_API_SECRET_SWING, BYBIT_API_KEY_SWING2, BYBIT_API_SECRET_SWING2, BYBIT_API_KEY_SWING3, BYBIT_API_SECRET_SWING3
from pybit.unified_trading import HTTP


session = HTTP(
    testnet=False,
    api_key=BYBIT_API_KEY,
    api_secret=BYBIT_API_SECRET,
)
sessionIntra = HTTP(
    testnet=False,
    api_key=BYBIT_API_KEY_INTRA,
    api_secret=BYBIT_API_SECRET_INTRA,
)
sessionIntra2 = HTTP(
    testnet=False,
    api_key=BYBIT_API_KEY_INTRA2,
    api_secret=BYBIT_API_SECRET_INTRA2,
)
sessionIntra3 = HTTP(
    testnet=False,
    api_key=BYBIT_API_KEY_INTRA3,
    api_secret=BYBIT_API_SECRET_INTRA3,
)
sessionClassic = HTTP(
    testnet=False,
    api_key=BYBIT_API_KEY_CLASSIC,
    api_secret=BYBIT_API_SECRET_CLASSIC,
)
sessionClassic2 = HTTP(
    testnet=False,
    api_key=BYBIT_API_KEY_CLASSIC2,
    api_secret=BYBIT_API_SECRET_CLASSIC2,
)
sessionClassic3 = HTTP(
    testnet=False,
    api_key=BYBIT_API_KEY_CLASSIC3,
    api_secret=BYBIT_API_SECRET_CLASSIC3,
)
sessionSwing = HTTP(
    testnet=False,
    api_key=BYBIT_API_KEY_SWING,
    api_secret=BYBIT_API_SECRET_SWING,
)
sessionSwing2 = HTTP(
    testnet=False,
    api_key=BYBIT_API_KEY_SWING2,
    api_secret=BYBIT_API_SECRET_SWING2,
)
sessionSwing3 = HTTP(
    testnet=False,
    api_key=BYBIT_API_KEY_SWING3,
    api_secret=BYBIT_API_SECRET_SWING3,
)

MAIN = float(session.get_wallet_balance(accountType="SPOT")['result']['list'][0]['coin'][1]['walletBalance'])
INTRA = float(sessionIntra.get_wallet_balance(accountType="CONTRACT")['result']['list'][0]['coin'][0]['equity'])
CLASSIC = float(sessionClassic.get_wallet_balance(accountType="CONTRACT")['result']['list'][0]['coin'][0]['equity'])
SWING = float(sessionSwing.get_wallet_balance(accountType="CONTRACT")['result']['list'][0]['coin'][0]['equity'])
# Find a way to put equity = 0 if the wallet balance is empty for other wallets
# For now solution is to always have at least one dollar on each subbacount
INTRA2 = float(sessionIntra2.get_wallet_balance(accountType="CONTRACT")['result']['list'][0]['coin'][0]['equity'])
CLASSIC2 = float(sessionClassic2.get_wallet_balance(accountType="CONTRACT")['result']['list'][0]['coin'][0]['equity'])
SWING2 = float(sessionSwing3.get_wallet_balance(accountType="CONTRACT")['result']['list'][0]['coin'][0]['equity'])

INTRA3 = float(sessionIntra3.get_wallet_balance(accountType="CONTRACT")['result']['list'][0]['coin'][0]['equity'])
CLASSIC3 = float(sessionClassic3.get_wallet_balance(accountType="CONTRACT")['result']['list'][0]['coin'][0]['equity'])
SWING3 = float(sessionSwing3.get_wallet_balance(accountType="CONTRACT")['result']['list'][0]['coin'][0]['equity'])

print(MAIN, INTRA, CLASSIC, SWING, INTRA2, CLASSIC2, SWING2, INTRA3, CLASSIC3, SWING3)