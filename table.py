from prettytable import PrettyTable

from check_prices import check_prices


def create_table(coins_p2p_buy, coins_p2p_sell, coins_spot, coins_buy_percents, coins_sell_percents):

    th = ['COIN', '% input', 'p2p BUY', 'spot cost', 'p2p SELL', '% output']
    td = []
    for i in ['USDT', 'BTC', 'BUSD', 'BNB', 'ETH']:
        td.append(i)
        td.append(str(coins_buy_percents[i]) + '%')
        td.append(coins_p2p_buy[i])
        td.append(coins_spot[i])
        td.append(coins_p2p_sell[i])
        td.append(str(coins_sell_percents[i]) + '%')

    columns = len(th)

    table = PrettyTable(th)

    td_data = td[:]

    while td_data:
        table.add_row(td_data[:columns])
        td_data = td_data[columns:]

    return table

