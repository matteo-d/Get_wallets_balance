from config import BYBIT_API_KEY, BYBIT_API_SECRET
from pybit.unified_trading import HTTP
import uuid
import math

# CREATE SESSION TO USE USE API V5
session = HTTP(
    testnet=False,
    api_key=BYBIT_API_KEY,
    api_secret=BYBIT_API_SECRET,
)

# PRICE LEVELS INTERESTING
levels = [
    3806.0,
    6307.0,
    7925.5,
    10316.5,
    12831.0,
    16016.0,
    17770.0,
    18235.0,
    20093.0,
    21199.5,
    22914.0,
    23318.0,
    24350.5,
    26252.0,
    27953.5,
    28396.5,
    29168.0,
    29573.5,
    30021.0,
    32902.0,
    34760.5,
    36044.0,
    42960.5,
    46542.0,
    50733.0,
    57134.0,
    58876.0,
    61477.5
]

# MINIMUM POSITION SIZE IN COIN DENOMINATION
minimum_position = 0.001

# AVAILABLE BALANCE IN USDT
MAIN_BALANCE = float(session.get_wallet_balance(accountType="SPOT")[
    'result']['list'][0]['coin'][1]['walletBalance'])
print("TOTAL ON MAIN ACCOUNT", MAIN_BALANCE, "$ \n\n")

# GET VALUE IN USDT OF THE DESIRED POSITION IN USDT
allocation = (int(MAIN_BALANCE) * 0.2) - 1
print(allocation)

# GET CURRENT PRICE OF THE COIN
coin_infos = session.get_tickers(
    category="spot",
    symbol="BTCUSDT",
)
current_price = math.floor(float(coin_infos['result']['list'][0]['usdIndexPrice']))
print(current_price)

# FIND INDEX OF THE PRICE CLOSEST TO THE CURRENT PRICE OF THE COIN
def find_closest_index(arr, x):
    closest_index = min(range(len(arr)), key=lambda i: abs(arr[i] - x))
    return closest_index
closest_index = find_closest_index(levels, current_price)
print(f"The index of the element closest to {current_price} is: {closest_index}")

# DEFINE BETWEEN WHICH INDEX I WANT TO POST ORDER
end_index = closest_index
start_index = 5

def getIndexOfHighestOrder(x):
    # CALCULATE THE COST IN DOLLARS OF POSITIONING AT THE WANTED LEVELS
    sum_result = 0
    for i in range(start_index, x):
        sum_result += levels[i] * 0.001
    # CHECK IF COST IN DOLLARS IS LOWER THAN MY MAX SIZE
    result_ternary = 0 if sum_result > allocation  else 1
    # IF COST IN DOLLARS IS TOO HIGH THEN TRY AGAIN STARTING FROM AN INDEX LOWER
    if result_ternary == 0 :
        print("not enough funds")
        x - 1
        foo(end_index)

    print("enough_found")
    return end_index

end_index = getIndexOfHighestOrder(end_index)
print(end_index)