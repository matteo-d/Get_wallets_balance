"""from config import BYBIT_API_KEY, BYBIT_API_SECRET
from config import MAIN_ID,INTRA_ID,CLASSIC_ID,SWING_ID,INTRA2_ID,CLASSIC2_ID,SWING2_ID,INTRA3_ID,CLASSIC3_ID,SWING3_ID
from get_transferable_funds import INTRA_TRANSFERABLE, CLASSIC_TRANSFERABLE, SWING_TRANSFERABLE, INTRA2_TRANSFERABLE, CLASSIC2_TRANSFERABLE, SWING2_TRANSFERABLE, INTRA3_TRANSFERABLE, CLASSIC3_TRANSFERABLE, SWING3_TRANSFERABLE  
from get_balances import SHOULD_BE_ON_INTRAS, SHOULD_BE_ON_CLASSICS, SHOULD_BE_ON_SWINGS
import math
from pybit.unified_trading import HTTP
import uuid

session = HTTP(
    testnet=False,
    api_key=BYBIT_API_KEY,
    api_secret=BYBIT_API_SECRET,
)

from_member_ids = [INTRA_ID, CLASSIC_ID, SWING_ID, INTRA2_ID, CLASSIC2_ID, SWING2_ID, INTRA3_ID, CLASSIC3_ID, SWING3_ID]
amounts = [INTRA_TRANSFERABLE['result']['balance']['transferBalance'], CLASSIC_TRANSFERABLE['result']['balance']['transferBalance'], SWING_TRANSFERABLE['result']['balance']['transferBalance'], INTRA2_TRANSFERABLE['result']['balance']['transferBalance'], CLASSIC2_TRANSFERABLE['result']['balance']['transferBalance'], SWING2_TRANSFERABLE['result']['balance']['transferBalance'], INTRA3_TRANSFERABLE['result']['balance']['transferBalance'], CLASSIC3_TRANSFERABLE['result']['balance']['transferBalance'], SWING3_TRANSFERABLE['result']['balance']['transferBalance']]

to_intras = [INTRA_ID, INTRA2_ID, INTRA3_ID]

def fund_intra_accounts(session, to_intras):
    coin = "USDT"
    from_account_type = "SPOT"
    to_account_type = "CONTRACT"
    results_intras = []
    print(SHOULD_BE_ON_INTRAS)
    for to_intra in zip(to_intras):
        transfer_id = str(uuid.uuid4())
        ajusted_amount = math.floor(float(amount)) -1
        if ajusted_amount > 1 :
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
"""