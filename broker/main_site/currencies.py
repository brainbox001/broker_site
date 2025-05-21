# from binance.client import Client
# from dotenv import load_dotenv
# import os
# load_dotenv()


def get_tickers():
  coin_dict = {
    "Bitcoin(BTC)": [
        68500.00,    # askPrice
        -1.50,       # priceChangePercent (negative)
        'bitcoin',
        '#f70511',   # Red because negative
        ''           # Empty sign because negative
    ],
    "Etherium(ETH)": [
        3500.25,     # askPrice
        0.80,        # priceChangePercent (positive, but <= 1)
        'etherium',
        '#f70511',   # Red because 0 < change <= 1 (as per current code logic)
        '+'
    ],
    "Litecoin(LTC)": [
        80.10,       # askPrice
        2.50,        # priceChangePercent (positive, > 1)
        'litecoin',
        'green',     # Green because positive and > 1
        '+'
    ],
    "Tron(TRX)": [
        0.1234,      # askPrice
        -0.05,       # priceChangePercent (negative)
        'tron',
        '#f70511',   # Red because negative
        ''
    ],
    "Tether(USDT)": [
        1.0005678,   # Calculated: round(Bitcoin(BTC) price / BTCUSDT price, 7)
        0.02,        # Fixed value
        'tether',
        'red',       # Fixed value
        '+'          # Fixed value
    ]
}
#   API_KEY = os.getenv('API_KEY')
#   SECRET_KEY = os.getenv('SECRET_KEY')
#   client = Client(API_KEY, SECRET_KEY)
#   tickers = client.get_all_tickers()
#   coin_dict = {}
#   coins_list = ['BTCBUSD', 'ETHBUSD', 'LTCBUSD', 'TRXBUSD', 'BTCUSDT']
#   coin_names = ['Bitcoin', 'Etherium', 'Litecoin', 'Tron', 'Tether']
#   tickers2 = client.get_ticker()
#   usdt_price = 0
#   color = ''
#   sign = ''
#   for tick in tickers2:
#       for num in range(len(coin_names)):
#           if tick['symbol'] == coins_list[num]:
              
#             if float(tick['priceChangePercent']) < 0:
#                 color = '#f70511'
#                 sign = ''
#             elif 0 < float(tick['priceChangePercent']) <= 1:
#                 color = '#f70511'
#                 sign = '+'
#             else:
#                 sign = '+'
#                 color = 'green'
#             if tick['symbol'] == 'BTCUSDT':
#                 usdt_price = float(tick['askPrice'])
#             else:
#                 coin_dict[f'{coin_names[num]}({coins_list[num].replace("BUSD", "")})'] = [float(tick['askPrice']), float(tick['priceChangePercent']), coin_names[num].lower(), color, sign]
#   coin_dict['Tether(USDT)'] = [round(coin_dict['Bitcoin(BTC)'][0]/usdt_price, 7), 0.02, 'tether', 'red', '+']
  return coin_dict
