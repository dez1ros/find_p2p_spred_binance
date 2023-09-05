from check_prices import check_prices
from coin_price import get_coin_price


def find_spread_p2p(coins_p2p_buy, coins_p2p_sell, coins_spot, coins_buy_percents, coins_sell_percents):
    coins_p2p_buy = coins_p2p_buy
    coins_p2p_sell = coins_p2p_sell
    coins = ['USDT', 'BTC', 'BUSD', 'BNB', 'ETH']

    sviazki = []

    for i in coins:
        for j in coins:
            if i != j:
                st = 10000
                st /= coins_p2p_buy[i]
                st *= get_coin_price(i, j)
                st *= coins_p2p_sell[j]
                if 0 < (st - 10000) / 10000:
                    sviazki.append((str(i) + '/' + str(j), (st - 10000) / 10000 * 100))
    if len(sviazki) == 0:
        return [('отмена', 'p2p связки не найдены')]

    return sviazki


def find_spread_p2p_spot_rub(coins_p2p_buy, coins_p2p_sell, coins_spot, coins_buy_percents, coins_sell_percents):
    coins = ['USDT', 'BTC', 'BUSD', 'BNB', 'ETH']
    rubs_coins = ['ADA', 'ALGO', 'ARB', 'ARPA', 'BNB', 'BTC', 'BUSD', 'DOT', 'ETH', 'LTC', 'MATIC', 'NEAR', 'NEO',
                  'SOL', 'XRP']
    sviazki = []

    for i in coins:
        for j in rubs_coins:
            try:
                st = 10000
                st /= coins_p2p_buy[i]
                st *= get_coin_price(i, j)
                st *= 0.999
                st *= get_coin_price(j, 'RUB')
                st *= 0.999
                if (st - 10000) / 10000 * 100 > -1 * 2:
                    sviazki.append((str(i) + '/' + str(j) + '=> RUB', (st - 10000) / 10000 * 100))
            except:
                pass
    if len(sviazki) == 0:
        return [('отмена', 'Связки со спотом в рубли не найдены')]

    return sviazki


def find_spread_p2p_spot_p2p(coins_p2p_buy, coins_p2p_sell, coins_spot, coins_buy_percents, coins_sell_percents):
    coins = ['USDT', 'BTC', 'BUSD', 'BNB', 'ETH']
    coins_2 = ['ADA', 'ALGO', 'ARB', 'ARPA', 'BNB', 'BTC', 'BUSD', 'DOT', 'ETH', 'LTC', 'MATIC', 'NEAR', 'NEO',
               'SOL', 'XRP']
    # coins_2 = ['DOT', 'ADA', 'AGIX', 'BETA', 'NKN', '1INCH', 'AAVE', 'ACA', 'ACH', 'ACM', 'ADX', 'AERGO', 'AGLD',
    #            'AKRO',
    #            'ALCX', 'ALGO', 'ALICE', 'ALPACA', 'ALPHA', 'ALPINE', 'AMB', 'AMB', 'ANKR', 'ANT', 'APE', 'API3', 'APT',
    #            'AR',
    #            'ARB', 'ARDR', 'ARK', 'ARPA', 'ARS', 'ASR', 'ASTR', 'ATA', 'ATM', 'ATOM', 'AUCTION', 'AUD', 'AUDIO',
    #            'AVA',
    #            'AVAX', 'AXS', 'BADGER', 'BAKE', 'BAL', 'BAND', 'BAR', 'BAT', 'BCH', 'BEL', 'BETH', 'BGBP', 'BICO',
    #            'BIDR',
    #            'BIFI', 'BLZ', 'BNB', 'BNT', 'BNX', 'BOND', 'BRL', 'BSW', 'BTC', 'BTS', 'BTTC', 'BTTOLD', 'BUSD',
    #            'C98', 'BURGER', 'CAKE', 'CELO', 'CELR', 'CFX', 'CHESS', 'CHR', 'CHZ', 'CITY', 'CKB', 'CLV', 'COMP',
    #            'COD',
    #            'COS', 'COTI', 'CREAM', 'CRV', 'CTK', 'CTSI', 'CTXC', 'CVC', 'CVP', 'CVX', 'DAI', 'DAR', 'DASH', 'DATA',
    #            'DCR',
    #            'DEGO', 'DENT', 'DEXE', 'DF', 'DGB', 'DIA', 'DOCK', 'DODO', 'DOGE', 'DREP', 'DUSK', 'DYDX', 'EDU',
    #            'EGLD',
    #            'ELF', 'ENJ', 'ENS', 'EOS', 'EPX', 'ERN', 'ETH', 'ETHW', 'EUR', 'FARM', 'FET', 'FIDA', 'FIL', 'FIO',
    #            'FIRO',
    #            'FIS', 'FLM', 'FLOKI', 'FLOW', 'FLR', 'FLUX', 'FOR', 'FORTH', 'FRONT', 'FTM', 'FTT', 'FUN', 'FXS', 'GAL',
    #            'GALA', 'GAS', 'GBT', 'GFT', 'GHST', 'GLM', 'GMT', 'GMX', 'GNS', 'GRT', 'GXS', 'HARD', 'HBAR', 'HFT',
    #            'HIFI',
    #            'HIGH', 'HIVE', 'HOOK', 'HOT', 'ICP', 'ICX', 'ID', 'IDEX', 'ILV', 'IMX', 'INJ', 'IOST', 'IOTA', 'IOTX',
    #            'IRIS',
    #            'JASMY', 'JOE', 'JST', 'JUV', 'KAVA', 'KDA', 'KEY', 'KLAY', 'KMD', 'KNC', 'KP3R', 'KSM', 'LAZIO', 'LDO',
    #            'LEVER', 'LINA', 'LINK', 'LIT', 'LOKA', 'LOOM', 'LPT', 'LQTY', 'LRC', 'LSK', 'LTC', 'LTO', 'LUNA',
    #            'LUNC',
    #            'MAGIC', 'MANA', 'MASK', 'MATIC', 'MBL', 'MBOX', 'MC', 'MDT', 'MDX', 'MINA', 'MKR', 'MLN', 'MOB', 'MOVR',
    #            'MTL', 'MULTI', 'NEAR', 'NEO', 'NEXO', 'NGN', 'NMR', 'NULS', 'OCEAN', 'OG', 'OGN', 'OM', 'OMG', 'ONG',
    #            'ONT',
    #            'OOLI', 'OP', 'ORN', 'OSMO', 'OXT', 'PAX', 'PAXG', 'PEOPLE', 'PEPE', 'PERL', 'PERP', 'PHA', 'PHB',
    #            'PIVX',
    #            'PLA', 'PLN', 'PNT', 'POLS', 'POLUX', 'POND', 'POWR', 'PROM', 'PROS', 'PSG', 'PUNDIX', 'PYR', 'QI',
    #            'QKC',
    #            'QNT', 'QTUM', 'QUICK', 'RAD', 'RARE', 'RAY', 'RDNT', 'RDNTOLD', 'REEF', 'REI', 'REN', 'REQ', 'RIF',
    #            'RLC',
    #            'RNDR', 'RON', 'ROSE', 'RPL', 'RSR', 'RUB', 'RUNE', 'RVN', 'SAND', 'SANTOS', 'SC', 'SCRT', 'SFP', 'SHIB',
    #            'SKL', 'SLP', 'SNM', 'SNT', 'SNX', 'SOL', 'SPELL', 'SRM', 'SSV', 'STEEM', 'STG', 'STGOLD', 'STMX',
    #            'STORJ',
    #            'STPT', 'STRAX', 'STX', 'SUI', 'SUN', 'SUPER', 'SUSHI', 'SXP', 'SYS', 'T', 'TFUEL', 'THETA', 'TKO',
    #            'TLM',
    #            'TOMO', 'TORN', 'TRB', 'TRU', 'TRX', 'TRY', 'TUSD', 'TVK', 'TWT', 'UAH', 'UFT', 'UMA', 'UNFI', 'UNI',
    #            'USDC',
    #            'USDP', 'USDT', 'USTC', 'UTK', 'VET', 'VGX', 'VIB', 'VIDT', 'VITE', 'VOXEL', 'VTHO', 'WAN', 'WAVES',
    #            'WAXP',
    #            'WBNB', 'WBTC', 'WETH', 'WIN', 'WING', 'WNXM', 'WOO', 'WRX', 'WTC', 'XEC', 'XEM', 'XLM', 'XMR', 'XNO',
    #            'XRP',
    #            'XTZ', 'XVG', 'XVS', 'YFI', 'YFII', 'YGG', 'ZAR', 'ZEC', 'ZEN', 'ZIL', 'ZRX']
    sviazki = []

    for i in coins:
        for j in coins_2:
            try:
                st = 10000
                st /= coins_p2p_buy[i]
                st *= get_coin_price(i, j)
                st *= 0.999
                st2 = st
                for ij in coins:
                    if ij != i and ij != j:
                        st *= get_coin_price(j, ij)
                        st *= 0.999
                        st *= coins_p2p_sell[ij]
                        if (st - 10000) / 10000 * 100 > 0:
                            sviazki.append((str(i) + '/' + str(j) + '=>' + str(ij), (st - 10000) / 10000 * 100))
                        st = st2
            except:
                pass
    if len(sviazki) == 0:
        return [('отмена', 'Связки со спотом в p2p не найдены')]

    return sviazki
#
#
# prices = ({'USDT': 89.73, 'BTC': 2735000.0, 'BUSD': 89.77, 'BNB': 20998.99, 'ETH': 166928.37},
#           {'USDT': 89.65, 'BTC': 2733250.17, 'BUSD': 89.54, 'BNB': 20842.57, 'ETH': 165635.21},
#           {'USDT': 87.32, 'BTC': 2667187.0, 'BUSD': 87.37, 'BNB': 20379.19, 'ETH': 161709.1},
#           {'USDT': -2.69, 'BTC': -2.48, 'BUSD': -2.67, 'BNB': -2.95, 'ETH': -3.13},
#           {'USDT': 2.67, 'BTC': 2.48, 'BUSD': 2.48, 'BNB': 2.27, 'ETH': 2.43})
#
# print(find_spread_p2p_spot_p2p(*prices))
