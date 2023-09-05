# import pandas as pd
# import requests
# from pprint import pprint
# import json
#
#
# def get_p2p_page(url, page, rows, coin, action):
#     headers = {'content-type': 'application/json'}
#     json_data = {
#         "page": page,
#         "rows": rows,
#         "asset": coin,
#         "fiat": "RUB",
#         "tradeType": action,
#     }
#     response = requests.post(url, headers=headers, json=json_data)
#     if response.status_code != 200:
#         response.raise_for_status()
#     return json.loads(response.text)
#
#
# def get_p2p_price(coin, action, summa):
#     url = r'https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search'
#     min_price = ''
#     page = 0
#     flag = 0
#     while not min_price:
#         page += 1
#         r = get_p2p_page(url, page, 1, coin, action.upper())
#         if r['data'] == []:
#             break
#         for i in r['data']:
#             for j in range(len(i['adv']['tradeMethods'])):
#                 if (i['adv']['tradeMethods'][j]['tradeMethodName'] == 'Tinkoff' or i['adv']['tradeMethods'][j][
#                     'tradeMethodName'] == 'RosBank') and float(i['adv']['minSingleTransAmount']) <= summa + 1:
#                     min_price = i['adv']['price']
#                     flag = 1
#                     break
#             if flag == 1:
#                 break
#
#     return float(min_price)