# BOMBA HAKASH

# After sending funds to Spot
# Get equity on exchange
from config import BYBIT_API_KEY, BYBIT_API_SECRET
from get_balances import  MAIN_BALANCE
from config import MAIN_ID,INTRA_ID,CLASSIC_ID,SWING_ID,INTRA2_ID,CLASSIC2_ID,SWING2_ID,INTRA3_ID,CLASSIC3_ID,SWING3_ID
from pybit.unified_trading import HTTP
import uuid

session = HTTP(
    testnet=False,
    api_key=BYBIT_API_KEY,
    api_secret=BYBIT_API_SECRET,
)

def fund_swing(session):
    coin = "USDT"
    from_account_type = "SPOT"
    to_account_type = "CONTRACT"
    amount = int(MAIN_BALANCE) - 1
    transfer_id = str(uuid.uuid4())
    result_swing = session.create_universal_transfer(
        transferId=transfer_id,
        coin=coin,
        amount=str(amount),
        fromMemberId=MAIN_ID,
        toMemberId=SWING_ID, 
        fromAccountType=from_account_type,
        toAccountType=to_account_type
    )
    return result_swing

result_swing = fund_swing(session)
print(result_swing)