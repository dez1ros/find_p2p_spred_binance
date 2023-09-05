import time
from prettytable import PrettyTable

from coin_price import get_coin_price, get_p2p_price
from check_prices import check_prices
from table import create_table

summa = 5000

start = time.time()

p2pUSDTbuy = get_p2p_price('USDT', 'BUY', summa)
p2pBTCbuy = get_p2p_price('BTC', 'BUY', summa)
p2pBUSDbuy = get_p2p_price('BUSD', 'BUY', summa)
p2pBNBbuy = get_p2p_price('BNB', 'BUY', summa)
p2pETHbuy = get_p2p_price('ETH', 'BUY', summa)
p2pRUBbuy = get_p2p_price('RUB', 'BUY', summa)
# p2pSHIBbuy = get_p2p_price('SHIB', 'BUY', summa)

p2pUSDTsell = get_p2p_price('USDT', 'SELL', summa)
p2pBTCsell = get_p2p_price('BTC', 'SELL', summa)
p2pBUSDsell = get_p2p_price('BUSD', 'SELL', summa)
p2pBNBsell = get_p2p_price('BNB', 'SELL', summa)
p2pETHsell = get_p2p_price('ETH', 'SELL', summa)
p2pRUBsell = get_p2p_price('RUB', 'SELL', summa)
# p2pSHIBsell = get_p2p_price('SHIB', 'SELL', summa)

spotUSDT = get_coin_price('USDT', 'RUB')
spotBTC = get_coin_price('BTC', 'RUB')
spotBUSD = get_coin_price('BUSD', 'RUB')
spotBNB = get_coin_price('BNB', 'RUB')
spotETH = get_coin_price('ETH', 'RUB')
# spotSHIB = get_coin_price('SHIB', 'rub')

th = ['COIN', '% input', 'p2p BUY', 'spot cost', 'p2p SELL', '% output']
td = [
    'USDT', (spotUSDT - p2pUSDTbuy) / p2pUSDTbuy * 100, p2pUSDTbuy, spotUSDT, p2pUSDTsell,
            (p2pUSDTsell - spotUSDT) / spotUSDT * 100,
    'BTC', (spotBTC - p2pBTCbuy) / p2pBTCbuy * 100, p2pBTCbuy, spotBTC, p2pBTCsell,
            (p2pBTCsell - spotBTC) / spotBTC * 100,
    'BUSD', (spotBUSD - p2pBUSDbuy) / p2pBUSDbuy * 100, p2pBUSDbuy, spotBUSD, p2pBUSDsell,
            (p2pBUSDsell - spotBUSD) / spotBUSD * 100,
    'BNB', (spotBNB - p2pBNBbuy) / p2pBNBbuy * 100, p2pBNBbuy, spotBNB, p2pBNBsell,
            (p2pBNBsell - spotBNB) / spotBNB * 100,
    'ETH', (spotETH - p2pETHbuy) / p2pETHbuy * 100, p2pETHbuy, spotETH, p2pETHsell,
            (p2pETHsell - spotETH) / spotETH * 100
]

columns = len(th)

table = PrettyTable(th)

td_data = td[:]

while td_data:
    table.add_row(td_data[:columns])
    td_data = td_data[columns:]

print(table)  # Печатаем таблицу

end = time.time()

print("The time of execution of above program is :",
      (end - start) * 10 ** 3 / 1000, "sec")

coins = ['usdt', 'btc', 'busd', 'bnb', 'eth']
coins_buy = {'usdt': p2pUSDTbuy, 'btc': p2pBTCbuy, 'busd': p2pBUSDbuy, 'bnb': p2pBNBbuy, 'eth': p2pETHbuy}
coins_sell = {'usdt': p2pUSDTsell, 'btc': p2pBTCsell, 'busd': p2pBUSDsell, 'bnb': p2pBNBsell, 'eth': p2pETHsell}
coins_persents = {'usdt': (spotUSDT - p2pUSDTbuy) / p2pUSDTbuy * 100, 'btc': (spotBTC - p2pBTCbuy) / p2pBTCbuy * 100,
                  'busd': (spotBUSD - p2pBUSDbuy) / p2pBUSDbuy * 100, 'bnb': (spotBNB - p2pBNBbuy) / p2pBNBbuy * 100,
                  'eth': (spotETH - p2pETHbuy) / p2pETHbuy * 100}
for i in coins:
    for j in coins:
        if j != i:
            st = 10000
            st /= coins_buy[i]
            st /= get_coin_price(i, j)
            st *= coins_sell[j]
            if 0 < (st - 10000) / 10000 < 10:
                print(i + '/' + j)
                print((st - 10000) / 10000 * 100)

rubs_coins = ['ADA', 'ALGO', 'ARB', 'ARPA', 'BNB', 'BTC', 'BUSD', 'DOT', 'ETH', 'LTC', 'MATIC', 'NEAR', 'NEO', 'SOL',
              'XRP']
best = max(coins_persents, key=coins_persents.get)
print(best)
for i in rubs_coins:
    try:
        st = 10000
        st /= coins_buy[best]
        st /= get_coin_price(i, best)
        st *= get_coin_price(i, 'rub')
        print(i)
        print((st - 10000) / 10000 * 100)
    except:
        pass
