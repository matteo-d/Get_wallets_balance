from config import BYBIT_API_KEY, BYBIT_API_SECRET
from config import MAIN_ID,INTRA_ID,CLASSIC_ID,SWING_ID,INTRA2_ID,CLASSIC2_ID,SWING2_ID,INTRA3_ID,CLASSIC3_ID,SWING3_ID
from get_balances import MAIN_BALANCE, INTRA_BALANCE, CLASSIC_BALANCE, SWING_BALANCE, INTRA2_BALANCE, CLASSIC2_BALANCE, SWING2_BALANCE, INTRA3_BALANCE, CLASSIC3_BALANCE, SWING3_BALANCE
from get_balances import TOTAL_BALANCE_ON_EXCHANGE, TOTAL_STACK, SHOULD_BE_ON_EXCHANGE, SHOULD_BE_ON_INTRAS, SHOULD_BE_ON_CLASSICS, SHOULD_BE_ON_SWINGS

from pybit.unified_trading import HTTP
import uuid

session = HTTP(
    testnet=False,
    api_key=BYBIT_API_KEY,
    api_secret=BYBIT_API_SECRET,
)

print("TOTAL ON MAIN ACCOUNT",MAIN_BALANCE, "$ \n\n","TOTAL ON INTRA ACCOUNT",INTRA_BALANCE,"$ \n","TOTAL ON CLASSIC ACCOUNT",CLASSIC_BALANCE,"$ \n","TOTAL ON SWING ACCOUNT",SWING_BALANCE,"$ \n","TOTAL ON INTRA2 ACCOUNT",INTRA2_BALANCE,"$ \n","TOTAL ON CLASSIC2 ACCOUNT",CLASSIC2_BALANCE,"$ \n","TOTAL ON SWING2 ACCOUNT",SWING2_BALANCE,"$ \n","TOTAL ON INTRA3 ACCOUNT",INTRA3_BALANCE,"$ \n","TOTAL ON CLASSIC3 ACCOUNT",CLASSIC3_BALANCE,"$ \n","TOTAL ON SWING3 ACCOUNT",SWING3_BALANCE,"$ \n")
print("SHOULD BE ON INTRAS", SHOULD_BE_ON_INTRAS, "$ \n","SHOULD BE ON CLASSICS", SHOULD_BE_ON_CLASSICS, "$ \n","SHOULD BE ON SWINGS", SHOULD_BE_ON_SWINGS, "$ \n")
print("TOTAL BALANCE ON EXCHANGE : ", TOTAL_BALANCE_ON_EXCHANGE, "$")
print("SHOULD BE ON EXCHANGE : ", SHOULD_BE_ON_EXCHANGE, "$")
print("TOTAL STACK : ", TOTAL_STACK,"$ \n" )

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
        result = session.create_universal_transfer(
            transferId=transfer_id,
            coin=coin,
            amount=str(amount - 1),
            fromMemberId=from_member_id,
            toMemberId=MAIN_ID,  # Assuming MAIN_ID is defined somewhere in your code
            fromAccountType=from_account_type,
            toAccountType=to_account_type
        )
        results.append(result)

    return results

from_member_ids = [INTRA_ID, CLASSIC_ID, SWING_ID, INTRA2_ID, CLASSIC2_ID, SWING2_ID, INTRA3_ID, CLASSIC2_ID, SWING3_ID]
amounts = [INTRA_BALANCE, CLASSIC_BALANCE, SWING_BALANCE, INTRA2_BALANCE, CLASSIC2_BALANCE, SWING2_BALANCE, INTRA3_BALANCE, CLASSIC3_BALANCE, SWING3_BALANCE]

results = fund_spot_account(session, from_member_ids, amounts)

for result in results:
    print(result)
