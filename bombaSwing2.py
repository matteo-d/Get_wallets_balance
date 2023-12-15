# After sending funds to Spot
# Get equity on exchange
from get_balances import SHOULD_BE_ON_INTRAS, SHOULD_BE_ON_CLASSICS, SHOULD_BE_ON_SWINGS
from config import BYBIT_API_KEY, BYBIT_API_SECRET, SWING2_ID, MAIN_ID
from pybit.unified_trading import HTTP
import uuid

session = HTTP(
    testnet=False,
    api_key=BYBIT_API_KEY,
    api_secret=BYBIT_API_SECRET,
)

# Transfer 1/3 to swing
def fund_account(session):
    coin = "USDT"
    from_account_type = "SPOT"
    to_account_type = "CONTRACT"
    amount = int(SHOULD_BE_ON_INTRAS) + int(SHOULD_BE_ON_CLASSICS) + int(SHOULD_BE_ON_SWINGS)
    transfer_id = str(uuid.uuid4())
    result = session.create_universal_transfer(
        transferId=transfer_id,
        coin=coin,
        amount=str(amount),
        fromMemberId=MAIN_ID,
        toMemberId=SWING2_ID, 
        fromAccountType=from_account_type,
        toAccountType=to_account_type
    )
    return result

result = fund_account(session)
print(result)