from config import BYBIT_API_KEY, BYBIT_API_SECRET
from config import MAIN_ID,INTRA_ID,CLASSIC_ID,SWING_ID,INTRA2_ID,CLASSIC2_ID,SWING2_ID,INTRA3_ID,CLASSIC3_ID,SWING3_ID
from get_transferable_funds import INTRA_TRANSFERABLE, CLASSIC_TRANSFERABLE, SWING_TRANSFERABLE, INTRA2_TRANSFERABLE, CLASSIC2_TRANSFERABLE, SWING2_TRANSFERABLE, INTRA3_TRANSFERABLE, CLASSIC3_TRANSFERABLE, SWING3_TRANSFERABLE  

from pybit.unified_trading import HTTP
import uuid

session = HTTP(
    testnet=False,
    api_key=BYBIT_API_KEY,
    api_secret=BYBIT_API_SECRET,
)
# SENDING ALL AVAILABLE FUNDS ON SUBBACOUNTS TO MAIN ACCOUNT

def fund_spot_account(session, from_member_ids, amounts):
    if len(from_member_ids) != len(amounts):
        raise ValueError("Length of from_member_ids and amounts lists must be the same.")

    coin = "USDT"
    from_account_type = "CONTRACT"
    to_account_type = "SPOT"

    results = []

    for from_member_id, amount in zip(from_member_ids, amounts):
        transfer_id = str(uuid.uuid4())
        if int(float(amount)) > 1:
            result = session.create_universal_transfer(
                transferId=transfer_id,
                coin=coin,
                amount=str(amount),
                fromMemberId=from_member_id,
                toMemberId=MAIN_ID, 
                fromAccountType=from_account_type,
                toAccountType=to_account_type
            )
            results.append(result)
        else :
            print("Less than 1$")
    return results

from_member_ids = [INTRA_ID, CLASSIC_ID, SWING_ID, INTRA2_ID, CLASSIC2_ID, SWING2_ID, INTRA3_ID, CLASSIC3_ID, SWING3_ID]
amounts = [INTRA_TRANSFERABLE['result']['balance']['transferBalance'], CLASSIC_TRANSFERABLE['result']['balance']['transferBalance'], SWING_TRANSFERABLE['result']['balance']['transferBalance'], INTRA2_TRANSFERABLE['result']['balance']['transferBalance'], CLASSIC2_TRANSFERABLE['result']['balance']['transferBalance'], SWING2_TRANSFERABLE['result']['balance']['transferBalance'], INTRA3_TRANSFERABLE['result']['balance']['transferBalance'], CLASSIC3_TRANSFERABLE['result']['balance']['transferBalance'], SWING3_TRANSFERABLE['result']['balance']['transferBalance']]
print(amounts)
results = fund_spot_account(session, from_member_ids, amounts)

for result in results:
    print(result)
