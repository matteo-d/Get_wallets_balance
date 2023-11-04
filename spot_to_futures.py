from config import BYBIT_API_KEY, BYBIT_API_SECRET
from config import MAIN_ID,INTRA_ID,CLASSIC_ID,SWING_ID,INTRA2_ID,CLASSIC2_ID,SWING2_ID,INTRA3_ID,CLASSIC3_ID,SWING3_ID
from get_transferable_funds import MAIN_TRANSFERABLE
from get_balances import MAIN_BALANCE
from get_balances import SHOULD_BE_ON_INTRAS, SHOULD_BE_ON_CLASSICS, SHOULD_BE_ON_SWINGS

from pybit.unified_trading import HTTP
import uuid

session = HTTP(
    testnet=False,
    api_key=BYBIT_API_KEY,
    api_secret=BYBIT_API_SECRET,
)

# FUNDS INTRAS ACCOUNTS
to_intras = [INTRA_ID, INTRA2_ID, INTRA3_ID]

def fund_intra_accounts(session, to_intras):
    coin = "USDT"
    from_account_type = "SPOT"
    to_account_type = "CONTRACT"
    results_intras = []
    print(SHOULD_BE_ON_INTRAS)
    for to_intra in zip(to_intras):
        transfer_id = str(uuid.uuid4())
        result = session.create_universal_transfer(
            transferId=transfer_id,
            coin=coin,
            amount=str(int(SHOULD_BE_ON_INTRAS)),
            fromMemberId=MAIN_ID,
            toMemberId=to_intra, 
            fromAccountType=from_account_type,
            toAccountType=to_account_type
        )
        results_intras.append(result)
    return results_intras

results_intras = fund_intra_accounts(session, to_intras)

for result in results_intras:
    print(result)

# FUNDS CLASSIC ACCOUNTS
to_classics = [CLASSIC_ID, CLASSIC2_ID, CLASSIC3_ID]

def fund_classic_accounts(session, to_classics):
    coin = "USDT"
    from_account_type = "SPOT"
    to_account_type = "CONTRACT"
    results_classic = []
    print(SHOULD_BE_ON_CLASSICS)
    for to_classic in zip(to_classics):
        transfer_id = str(uuid.uuid4())
        result = session.create_universal_transfer(
            transferId=transfer_id,
            coin=coin,
            amount=str(int(SHOULD_BE_ON_CLASSICS)),
            fromMemberId=MAIN_ID,
            toMemberId=to_classic, 
            fromAccountType=from_account_type,
            toAccountType=to_account_type
        )
        results_classic.append(result)
    return results_classic

results_classic = fund_classic_accounts(session, to_classics)

for result in results_classic:
    print(result)

# FUNDS SWING ACCOUNTS
to_swings = [SWING_ID, SWING2_ID, SWING3_ID]
print(SHOULD_BE_ON_SWINGS)
def fund_swing_accounts(session, to_swings):
    coin = "USDT"
    from_account_type = "SPOT"
    to_account_type = "CONTRACT"
    results_swing = []
    for to_swing in zip(to_swings):
        transfer_id = str(uuid.uuid4())
        result = session.create_universal_transfer(
            transferId=transfer_id,
            coin=coin,
            amount=str(int(SHOULD_BE_ON_SWINGS)),
            fromMemberId=MAIN_ID,
            toMemberId=to_swing, 
            fromAccountType=from_account_type,
            toAccountType=to_account_type
        )
        results_swing.append(result)
    return results_swing

results_swing = fund_swing_accounts(session, to_swings)

for result in results_swing:
    print(result)