from p2p_price import get_p2p_price
from coin_price import get_coin_price

summa = 10000

p2pUSDTbuy = get_p2p_price('USDT', 'BUY', summa)
p2pBTCbuy = get_p2p_price('BTC', 'BUY', summa)
p2pBUSDbuy = get_p2p_price('BUSD', 'BUY', summa)
p2pBNBbuy = get_p2p_price('BNB', 'BUY', summa)
p2pETHbuy = get_p2p_price('ETH', 'BUY', summa)


p2pRUBsell = get_p2p_price('RUB', 'SELL', summa)


coins_buy = {'usdt': p2pUSDTbuy, 'btc': p2pBTCbuy, 'busd': p2pBUSDbuy, 'bnb': p2pBNBbuy, 'eth': p2pETHbuy}
best = max(coins_buy, key=coins_buy.get)
print(best)
coins = ['DOT', 'ADA', 'AGIX', 'BETA', 'NKN', '1INCH', 'AAVE', 'ACA', 'ACH', 'ACM', 'ADX', 'AERGO', 'AGLD', 'AKRO',
         'ALCX', 'ALGO', 'ALICE', 'ALPACA', 'ALPHA', 'ALPINE', 'AMB', 'AMB', 'ANKR', 'ANT', 'APE', 'API3', 'APT', 'AR',
         'ARB', 'ARDR', 'ARK', 'ARPA', 'ARS', 'ASR', 'ASTR', 'ATA', 'ATM', 'ATOM', 'AUCTION', 'AUD', 'AUDIO', 'AVA',
         'AVAX', 'AXS', 'BADGER', 'BAKE', 'BAL', 'BAND', 'BAR', 'BAT', 'BCH', 'BEL', 'BETH', 'BGBP', 'BICO', 'BIDR',
         'BIFI', 'BLZ', 'BNB', 'BNT', 'BNX', 'BOND', 'BRL', 'BSW', 'BTC', 'BTS', 'BTTC', 'BTTOLD', 'BUSD',
         'C98', 'BURGER', 'CAKE', 'CELO', 'CELR', 'CFX', 'CHESS', 'CHR', 'CHZ', 'CITY', 'CKB', 'CLV', 'COMP', 'COD',
         'COS', 'COTI', 'CREAM', 'CRV', 'CTK', 'CTSI', 'CTXC', 'CVC', 'CVP', 'CVX', 'DAI', 'DAR', 'DASH', 'DATA', 'DCR',
         'DEGO', 'DENT', 'DEXE', 'DF', 'DGB', 'DIA', 'DOCK', 'DODO', 'DOGE', 'DREP', 'DUSK', 'DYDX', 'EDU', 'EGLD',
         'ELF', 'ENJ', 'ENS', 'EOS', 'EPX', 'ERN', 'ETH', 'ETHW', 'EUR', 'FARM', 'FET', 'FIDA', 'FIL', 'FIO', 'FIRO',
         'FIS', 'FLM', 'FLOKI', 'FLOW', 'FLR', 'FLUX', 'FOR', 'FORTH', 'FRONT', 'FTM', 'FTT', 'FUN', 'FXS', 'GAL',
         'GALA', 'GAS', 'GBT', 'GFT', 'GHST', 'GLM', 'GMT', 'GMX', 'GNS', 'GRT', 'GXS', 'HARD', 'HBAR', 'HFT', 'HIFI',
         'HIGH', 'HIVE', 'HOOK', 'HOT', 'ICP', 'ICX', 'ID', 'IDEX', 'ILV', 'IMX', 'INJ', 'IOST', 'IOTA', 'IOTX', 'IRIS',
         'JASMY', 'JOE', 'JST', 'JUV', 'KAVA', 'KDA', 'KEY', 'KLAY', 'KMD', 'KNC', 'KP3R', 'KSM', 'LAZIO', 'LDO',
         'LEVER', 'LINA', 'LINK', 'LIT', 'LOKA', 'LOOM', 'LPT', 'LQTY', 'LRC', 'LSK', 'LTC', 'LTO', 'LUNA', 'LUNC',
         'MAGIC', 'MANA', 'MASK', 'MATIC', 'MBL', 'MBOX', 'MC', 'MDT', 'MDX', 'MINA', 'MKR', 'MLN', 'MOB', 'MOVR',
         'MTL', 'MULTI', 'NEAR', 'NEO', 'NEXO', 'NGN', 'NMR', 'NULS', 'OCEAN', 'OG', 'OGN', 'OM', 'OMG', 'ONG', 'ONT',
         'OOLI', 'OP', 'ORN', 'OSMO', 'OXT', 'PAX', 'PAXG', 'PEOPLE', 'PEPE', 'PERL', 'PERP', 'PHA', 'PHB', 'PIVX',
         'PLA', 'PLN', 'PNT', 'POLS', 'POLUX', 'POND', 'POWR', 'PROM', 'PROS', 'PSG', 'PUNDIX', 'PYR', 'QI', 'QKC',
         'QNT', 'QTUM', 'QUICK', 'RAD', 'RARE', 'RAY', 'RDNT', 'RDNTOLD', 'REEF', 'REI', 'REN', 'REQ', 'RIF', 'RLC',
         'RNDR', 'RON', 'ROSE', 'RPL', 'RSR', 'RUB', 'RUNE', 'RVN', 'SAND', 'SANTOS', 'SC', 'SCRT', 'SFP', 'SHIB',
         'SKL', 'SLP', 'SNM', 'SNT', 'SNX', 'SOL', 'SPELL', 'SRM', 'SSV', 'STEEM', 'STG', 'STGOLD', 'STMX', 'STORJ',
         'STPT', 'STRAX', 'STX', 'SUI', 'SUN', 'SUPER', 'SUSHI', 'SXP', 'SYS', 'T', 'TFUEL', 'THETA', 'TKO', 'TLM',
         'TOMO', 'TORN', 'TRB', 'TRU', 'TRX', 'TRY', 'TUSD', 'TVK', 'TWT', 'UAH', 'UFT', 'UMA', 'UNFI', 'UNI', 'USDC',
         'USDP', 'USDT', 'USTC', 'UTK', 'VET', 'VGX', 'VIB', 'VIDT', 'VITE', 'VOXEL', 'VTHO', 'WAN', 'WAVES', 'WAXP',
         'WBNB', 'WBTC', 'WETH', 'WIN', 'WING', 'WNXM', 'WOO', 'WRX', 'WTC', 'XEC', 'XEM', 'XLM', 'XMR', 'XNO', 'XRP',
         'XTZ', 'XVG', 'XVS', 'YFI', 'YFII', 'YGG', 'ZAR', 'ZEC', 'ZEN', 'ZIL', 'ZRX']

rubs_coins = ['ADA', 'ALGO', 'ARB', 'ARPA', 'BNB', 'BTC', 'BUSD', 'DOT', 'ETH', 'LTC', 'MATIC', 'NEAR', 'NEO', 'SOL',
              'XRP']

for i in rubs_coins:
    try:
        st = 10000
        st /= p2pUSDTbuy
        st /= get_coin_price(i, 'usdt')
        st *= get_coin_price(i, 'rub')
        print(i)
        print((st - 10000) / 10000 * 100)
    except:
        pass
