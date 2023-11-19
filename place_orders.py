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

# AVAILABLE BALANCE IN USDT
MAIN_BALANCE = float(session.get_wallet_balance(accountType="SPOT")[
    'result']['list'][0]['coin'][1]['walletBalance'])
print("TOTAL ON MAIN ACCOUNT", MAIN_BALANCE, "$ \n\n")

# GET VALUE IN USDT OF THE DESIRED POSITION IN USDT
allocation = (int(MAIN_BALANCE) * 0.2) - 1
print("Allocation : ", allocation)

# GET CURRENT PRICE OF THE COIN
coin_infos = session.get_tickers(
    category="spot",
    symbol="BTCUSDT",
)
current_price = math.floor(float(coin_infos['result']['list'][0]['usdIndexPrice']))
print("Current price : ", current_price)

# FIND INDEX OF THE PRICE CLOSEST TO THE CURRENT PRICE OF THE COIN
def find_closest_index(arr, x):
    closest_index = min(range(len(arr)), key=lambda i: abs(arr[i] - x))
    return closest_index
closest_index = find_closest_index(levels, current_price)
print(f"The index of the element closest to {current_price} is: {closest_index}")

# DEFINE BETWEEN WHICH INDEX I WANT TO POST ORDER
end_index = closest_index
start_index = 5
minimum_position_size = 0.001
print("Minimum position size : " , minimum_position_size)
def getIndexOfHighestOrder(x):
    # CALCULATE THE COST IN DOLLARS OF POSITIONING AT THE WANTED LEVELS
    totalcost = 0
    for i in range(start_index, x):
        totalcost += levels[i] * minimum_position_size
    # CHECK IF COST IN DOLLARS IS LOWER THAN MY MAX SIZE
    result_ternary = 0 if totalcost >= allocation  else 1
    # IF COST IN DOLLARS IS TOO HIGH THEN TRY AGAIN STARTING FROM AN INDEX LOWER
    if result_ternary == 0 :
        print(totalcost)
        print("Not enough funds for the desired distribution of orders : retrying ...")
        x - 1
        getIndexOfHighestOrder(end_index)

    print("Sum of prices * minimum position size : ",totalcost)
    print("Enough funds to distribute between levels")
    
    return end_index

end_index = getIndexOfHighestOrder(end_index)
print("End index of optimal price for optimizing distribution of orders : ",end_index)

# BETWEEN THE START INDEX OF LEVEL TO THE END INDEX FOUND WITH FUNCTION GETINDEXOFHIGHESTORDER 
# FIND THE MAX SIZE IN $ PER ORDER FOR THE PRICE LEVELS CONTAINED IN THE WANTED RANGE INSIDE THE LEVELS ARRAY
# ARRAY THAT CONTAIN ONLY THE RANGE OF WANTED LEVELS
arrayWantedLevels = levels[start_index:end_index]
print("Array of wanted levels : " , arrayWantedLevels)
print("Minimum position size : ", minimum_position_size)
print ("Max allocation : ", allocation)

def calculate_allocation(price, min_quantity, remaining_funds):
    # Calculate the maximum quantity based on remaining funds
    max_quantity = remaining_funds / price

    # Use the minimum quantity or the maximum quantity, whichever is smaller
    chosen_quantity = min(min_quantity, max_quantity)

    # Update the remaining funds after allocating
    remaining_funds -= chosen_quantity * price

    return chosen_quantity, remaining_funds

def optimal_allocations(prices, min_quantity, fund_limit):
    allocations = []
    remaining_funds = fund_limit

    for price in prices:
        quantity, remaining_funds = calculate_allocation(price, min_quantity, remaining_funds)
        allocations.append(quantity * price)

    return allocations


allocations = optimal_allocations(arrayWantedLevels, minimum_position_size, allocation)

print("Size in USDT per order : ", allocations)
print("Value in USDT of all orders : ", sum(allocations))
print("percentage of funds allocated : ", ( sum(allocations) / allocation) * 100, " %")


