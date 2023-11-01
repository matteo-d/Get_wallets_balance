from config import BYBIT_API_KEY, BYBIT_API_SECRET, BYBIT_API_KEY_INTRA, BYBIT_API_SECRET_INTRA, BYBIT_API_KEY_INTRA2, BYBIT_API_SECRET_INTRA2, BYBIT_API_KEY_INTRA3, BYBIT_API_SECRET_INTRA3, BYBIT_API_KEY_CLASSIC, BYBIT_API_SECRET_CLASSIC, BYBIT_API_KEY_CLASSIC2, BYBIT_API_SECRET_CLASSIC2, BYBIT_API_KEY_CLASSIC3, BYBIT_API_SECRET_CLASSIC3, BYBIT_API_KEY_SWING, BYBIT_API_SECRET_SWING, BYBIT_API_KEY_SWING2, BYBIT_API_SECRET_SWING2, BYBIT_API_KEY_SWING3, BYBIT_API_SECRET_SWING3
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
fromMemberId = 52392390,
toMemberId = 21419762,
fromAccountType = "CONTRACT",
toAccountType = "SPOT"
))