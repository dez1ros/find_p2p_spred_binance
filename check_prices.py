from coin_price import get_coin_price, get_p2p_price


def check_prices(summa):
    p2pUSDTbuy = get_p2p_price('USDT', 'BUY', summa)
    p2pBTCbuy = get_p2p_price('BTC', 'BUY', summa)
    p2pBUSDbuy = get_p2p_price('BUSD', 'BUY', summa)
    p2pBNBbuy = get_p2p_price('BNB', 'BUY', summa)
    p2pETHbuy = get_p2p_price('ETH', 'BUY', summa)
    p2pRUBbuy = get_p2p_price('RUB', 'BUY', summa)

    p2pUSDTsell = get_p2p_price('USDT', 'SELL', summa)
    p2pBTCsell = get_p2p_price('BTC', 'SELL', summa)
    p2pBUSDsell = get_p2p_price('BUSD', 'SELL', summa)
    p2pBNBsell = get_p2p_price('BNB', 'SELL', summa)
    p2pETHsell = get_p2p_price('ETH', 'SELL', summa)
    p2pRUBsell = get_p2p_price('RUB', 'SELL', summa)

    spotUSDT = get_coin_price('USDT', 'RUB')
    spotBTC = get_coin_price('BTC', 'RUB')
    spotBUSD = get_coin_price('BUSD', 'RUB')
    spotBNB = get_coin_price('BNB', 'RUB')
    spotETH = get_coin_price('ETH', 'RUB')

    coins_p2p_buy = {'USDT': p2pUSDTbuy, 'BTC': p2pBTCbuy, 'BUSD': p2pBUSDbuy, 'BNB': p2pBNBbuy, 'ETH': p2pETHbuy}
    coins_p2p_sell = {'USDT': p2pUSDTsell, 'BTC': p2pBTCsell, 'BUSD': p2pBUSDsell, 'BNB': p2pBNBsell, 'ETH': p2pETHsell}
    coins_spot = {'USDT': spotUSDT, 'BTC': spotBTC, 'BUSD': spotBUSD, 'BNB': spotBNB, 'ETH': spotETH}
    coins_buy_percents = {'USDT': round((spotUSDT - p2pUSDTbuy) / p2pUSDTbuy * 100, 2),
                          'BTC': round((spotBTC - p2pBTCbuy) / p2pBTCbuy * 100, 2),
                          'BUSD': round((spotBUSD - p2pBUSDbuy) / p2pBUSDbuy * 100, 2),
                          'BNB': round((spotBNB - p2pBNBbuy) / p2pBNBbuy * 100, 2),
                          'ETH': round((spotETH - p2pETHbuy) / p2pETHbuy * 100, 2)}
    coins_sell_percents = {'USDT': round((p2pUSDTsell - spotUSDT) / spotUSDT * 100, 2),
                           'BTC': round((p2pBTCsell - spotBTC) / spotBTC * 100, 2),
                           'BUSD': round((p2pBUSDsell - spotBUSD) / spotBUSD * 100, 2),
                           'BNB': round((p2pBNBsell - spotBNB) / spotBNB * 100, 2),
                           'ETH': round((p2pETHsell - spotETH) / spotETH * 100, 2)}

    return coins_p2p_buy, coins_p2p_sell, coins_spot, coins_buy_percents, coins_sell_percents
