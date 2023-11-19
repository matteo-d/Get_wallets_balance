# Get Wallets Balance
from config import  BYBIT_API_KEY_SWING3, BYBIT_API_SECRET_SWING3
from pybit.unified_trading import HTTP

sessionSwing3 = HTTP(
    testnet=False,
    api_key=BYBIT_API_KEY_SWING3,
    api_secret=BYBIT_API_SECRET_SWING3,
    recv_window=6000
)

SWING3_BALANCE = float(sessionSwing3.get_wallet_balance(accountType="CONTRACT", recv_window=6000)[
                 'result']['list'][0]['coin'][0]['equity'])

print(SWING3_BALANCE)