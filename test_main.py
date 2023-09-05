import time
from prettytable import PrettyTable

from coin_price import get_coin_price, get_p2p_price
from check_prices import check_prices
from table import create_table
from find_spread import find_spread_p2p, find_spread_p2p_spot_rub, find_spread_p2p_spot_p2p

start_time = time.time()

summa = 10000

prices = check_prices(summa)
prices = prices[:]

print(create_table(*prices))

print('p2p>p2p')
for i in find_spread_p2p(*prices):
    print(i[0])
    print(i[1])

# # не ликвид
# print('p2p>spot>rub')
# for i in find_spread_p2p_spot_rub(*prices):
#     print(i[0])
#     print(i[1])

# # тоже не ликвид
# print('p2p>spot>p2p')
# for i in find_spread_p2p_spot_p2p(*prices):
#     print(i[0])
#     print(i[1])


print("--- %s seconds ---" % (time.time() - start_time))
