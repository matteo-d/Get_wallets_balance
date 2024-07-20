# After sending funds to Spot
# Get equity on exchange
from config import BYBIT_API_KEY, BYBIT_API_SECRET
from get_balances import MAIN_BALANCE, TOTAL_BALANCE_ON_EXCHANGE
from config import MAIN_ID,INTRA_ID,CLASSIC_ID,SWING_ID,INTRA2_ID,CLASSIC2_ID,SWING2_ID,INTRA3_ID,CLASSIC3_ID,SWING3_ID
from pybit.unified_trading import HTTP


import uuid
import math

session = HTTP(
    testnet=False,
    api_key=BYBIT_API_KEY,
    api_secret=BYBIT_API_SECRET,
)
AMOUNT = math.floor((int(MAIN_BALANCE)- 1) / 6)
print(AMOUNT)
# FUNDS INTRAS ACCOUNTS
accounts = [INTRA_ID, INTRA2_ID, INTRA3_ID, CLASSIC_ID, CLASSIC2_ID]

def fund_intra_accounts(session, accounts):
    coin = "USDT"
    from_account_type = "SPOT"
    to_account_type = "CONTRACT"
    results = []
    for account in zip(accounts):
        transfer_id = str(uuid.uuid4())
        result = session.create_universal_transfer(
            transferId=transfer_id,
            coin=coin,
            amount=str(AMOUNT),
            fromMemberId=MAIN_ID,
            toMemberId=account, 
            fromAccountType=from_account_type,
            toAccountType=to_account_type
        )
        results.append(result)
    return results

results = fund_intra_accounts(session, accounts)

for result in results:
    print(result)
