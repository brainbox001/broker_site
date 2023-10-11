from binance.client import Client
from dotenv import load_dotenv
import os
load_dotenv()


def get_tickers():
  API_KEY = os.getenv('API_KEY')
  SECRET_KEY = os.getenv('SECRET_KEY')
  client = Client(API_KEY, SECRET_KEY)
  tickers = client.get_all_tickers()
  coin_dict = {}
  coins_list = ['BTCBUSD', 'ETHBUSD', 'LTCBUSD', 'TRXBUSD', 'BTCUSDT']
  coin_names = ['Bitcoin', 'Etherium', 'Litecoin', 'Tron', 'Tether']
  tickers2 = client.get_ticker()
  usdt_price = 0
  color = ''
  sign = ''
  for tick in tickers2:
      for num in range(len(coin_names)):
          if tick['symbol'] == coins_list[num]:
              
            if float(tick['priceChangePercent']) < 0:
                color = '#f70511'
                sign = ''
            elif 0 < float(tick['priceChangePercent']) <= 1:
                color = '#f70511'
                sign = '+'
            else:
                sign = '+'
                color = 'green'
            if tick['symbol'] == 'BTCUSDT':
                usdt_price = float(tick['askPrice'])
            else:
                coin_dict[f'{coin_names[num]}({coins_list[num].replace("BUSD", "")})'] = [float(tick['askPrice']), float(tick['priceChangePercent']), coin_names[num].lower(), color, sign]
  coin_dict['Tether(USDT)'] = [round(coin_dict['Bitcoin(BTC)'][0]/usdt_price, 7), 0.02, 'tether', 'red', '+']
  return coin_dict
