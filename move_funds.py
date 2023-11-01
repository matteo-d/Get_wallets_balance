from config import BYBIT_API_KEY, BYBIT_API_SECRET
from pybit.unified_trading import HTTP
import uuid

session = HTTP(
    testnet=False,
    api_key=BYBIT_API_KEY,
    api_secret=BYBIT_API_SECRET,
)

""" SHOULD USE CREATE UNIVERSAL TRANSFER ENDPOINT
transferId	true	string	UUID. Please manually generate a UUID
coin	true	string	Coin
amount	true	string	Amount
fromMemberId	true	integer	From UID
toMemberId	true	integer	To UID
fromAccountType	true	string	From account type
toAccountType	true	string	To account type 

HTTP Request
POST /v5/asset/transfer/universal-transfer
"""

print(session.create_universal_transfer(
transferId = str(uuid.uuid4()),
coin = "USDT",
amount = "10",
fromMemberId = 21419762,
toMemberId = 52392390,
fromAccountType = "SPOT",
toAccountType = "CONTRACT"
))