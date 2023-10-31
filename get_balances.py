# Get Wallets Balance
from config import BYBIT_API_KEY, BYBIT_API_SECRET, BYBIT_API_KEY_INTRA, BYBIT_API_SECRET_INTRA, BYBIT_API_KEY_INTRA2, BYBIT_API_SECRET_INTRA2, BYBIT_API_KEY_INTRA3, BYBIT_API_SECRET_INTRA3, BYBIT_API_KEY_CLASSIC, BYBIT_API_SECRET_CLASSIC, BYBIT_API_KEY_CLASSIC2, BYBIT_API_SECRET_CLASSIC2, BYBIT_API_KEY_CLASSIC3, BYBIT_API_SECRET_CLASSIC3, BYBIT_API_KEY_SWING, BYBIT_API_SECRET_SWING, BYBIT_API_KEY_SWING2, BYBIT_API_SECRET_SWING2, BYBIT_API_KEY_SWING3, BYBIT_API_SECRET_SWING3
from config import BANK
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

MAIN_BALANCE = float(session.get_wallet_balance(accountType="SPOT")[
             'result']['list'][0]['coin'][1]['walletBalance'])
INTRA_BALANCE = float(sessionIntra.get_wallet_balance(accountType="CONTRACT")[
              'result']['list'][0]['coin'][0]['equity'])
CLASSIC_BALANCE = float(sessionClassic.get_wallet_balance(accountType="CONTRACT")[
                'result']['list'][0]['coin'][0]['equity'])
SWING_BALANCE = float(sessionSwing.get_wallet_balance(accountType="CONTRACT")[
              'result']['list'][0]['coin'][0]['equity'])

INTRA2_BALANCE = float(sessionIntra2.get_wallet_balance(accountType="CONTRACT")[
               'result']['list'][0]['coin'][0]['equity'])
CLASSIC2_BALANCE = float(sessionClassic2.get_wallet_balance(accountType="CONTRACT")[
                 'result']['list'][0]['coin'][0]['equity'])
SWING2_BALANCE = float(sessionSwing3.get_wallet_balance(accountType="CONTRACT")[
               'result']['list'][0]['coin'][0]['equity'])

INTRA3_BALANCE = float(sessionIntra3.get_wallet_balance(accountType="CONTRACT")[
               'result']['list'][0]['coin'][0]['equity'])
CLASSIC3_BALANCE = float(sessionClassic3.get_wallet_balance(accountType="CONTRACT")[
                 'result']['list'][0]['coin'][0]['equity'])
SWING3_BALANCE = float(sessionSwing3.get_wallet_balance(accountType="CONTRACT")[
               'result']['list'][0]['coin'][0]['equity'])

TOTAL_BALANCE_ON_EXCHANGE = MAIN_BALANCE + INTRA_BALANCE + CLASSIC_BALANCE + SWING_BALANCE + INTRA2_BALANCE + CLASSIC2_BALANCE + SWING2_BALANCE + INTRA3_BALANCE + CLASSIC3_BALANCE + SWING3_BALANCE
TOTAL_STACK = TOTAL_BALANCE_ON_EXCHANGE + BANK * 1.06
SHOULD_BE_ON_EXCHANGE = TOTAL_STACK * 0.65
SHOULD_BE_ON_INTRAS = TOTAL_STACK * 0.0125
SHOULD_BE_ON_CLASSICS = TOTAL_STACK * 0.0375
SHOULD_BE_ON_SWINGS = TOTAL_STACK * 0.1125
print("TOTAL ON MAIN ACCOUNT",MAIN_BALANCE, "$ \n\n","TOTAL ON INTRA ACCOUNT",INTRA_BALANCE,"$ \n","TOTAL ON CLASSIC ACCOUNT",CLASSIC_BALANCE,"$ \n","TOTAL ON SWING ACCOUNT",SWING_BALANCE,"$ \n","TOTAL ON INTRA2 ACCOUNT",INTRA2_BALANCE,"$ \n","TOTAL ON CLASSIC2 ACCOUNT",CLASSIC2_BALANCE,"$ \n","TOTAL ON SWING2 ACCOUNT",SWING2_BALANCE,"$ \n","TOTAL ON INTRA3 ACCOUNT",INTRA3_BALANCE,"$ \n","TOTAL ON CLASSIC3 ACCOUNT",CLASSIC3_BALANCE,"$ \n","TOTAL ON SWING3 ACCOUNT",SWING3_BALANCE,"$ \n")
print("SHOULD BE ON INTRAS", SHOULD_BE_ON_INTRAS, "$ \n","SHOULD BE ON CLASSICS", SHOULD_BE_ON_CLASSICS, "$ \n","SHOULD BE ON SWINGS", SHOULD_BE_ON_SWINGS, "$ \n")
print("TOTAL BALANCE ON EXCHANGE : ", TOTAL_BALANCE_ON_EXCHANGE, "$")
print("SHOULD BE ON EXCHANGE : ", SHOULD_BE_ON_EXCHANGE, "$")
print("TOTAL STACK : ", TOTAL_STACK,"$ \n" )




