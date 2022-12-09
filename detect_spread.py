import ccxt
import pandas as pd
import time

pd.set_option('expand_frame_repr', True)  
pd.set_option("display.max_rows", 500)

from utils.Logger import get_logger
from configs.Config import BINANCE_CONFIG

class BA(ccxt.binance):

    def __init__(self):
        super().__init__(BINANCE_CONFIG)
        self.time_interval = 1
        self.quarterly_symbols_info = self.__get_quarterly_symbols_info()
        self.spot_fee_rate = 1/1000
        self.future_fee_rate = 1/10000

    def __get_quarterly_symbols_info(self):
        symbols = {}
        markets = self.load_markets()
        for symbol in self.dapiPublicGetExchangeInfo()['symbols']:
            future_symbol = symbol['symbol']
            # delivery date
            if '12' in future_symbol:
                spot_symbol = future_symbol[0:-10] + '/USDT'
                symbols[future_symbol[0:-10]] = (future_symbol,
                                                 int(symbol['pricePrecision']),  
                                                 int(symbol['contractSize']),  
                                                 spot_symbol,
                                                 markets[spot_symbol]['precision']['price'],  
                                                 markets[spot_symbol]['precision']['amount']) 

        return symbols

    def get_spread_info(self, logger):
        spot_future_spread = []
        for symbol_info in self.quarterly_symbols_info.values():
            symbol_future = symbol_info[0]
            symbol_spot = symbol_info[3]
            symbol_spot_temp = symbol_spot.replace('/', '')
            spot_buy1_price = float(self.publicGetTickerBookTicker(params={'symbol': symbol_spot_temp})['bidPrice'])
            spot_sell1_price = float(self.publicGetTickerBookTicker(params={'symbol': symbol_spot_temp})['askPrice'])
            future_buy1_price = float(
                self.dapiPublicGetTickerBookTicker(params={'symbol': symbol_future})[0]['bidPrice'])
            future_sell1_price = float(
                self.dapiPublicGetTickerBookTicker(params={'symbol': symbol_future})[0]['askPrice'])
            open_spread = future_buy1_price / spot_sell1_price - 1
            close_spread = future_sell1_price / spot_buy1_price - 1
            spot_future_spread.append((
                symbol_future, symbol_spot,
                open_spread,  
                future_buy1_price, spot_sell1_price,
                close_spread,  
                future_sell1_price, spot_buy1_price))

        df = pd.DataFrame(spot_future_spread)
        df.columns = ['symbol_future', 'symbol_spot',
                      'open_spread', 'future_buy1_price', 'spot_sell1_price',
                      'close_spread', 'future_sell1_price', 'spot_buy1_price']

        open_info = df[df['open_spread'] == df['open_spread'].max()].values[0].tolist()[0:5]

        close_info = df[df['close_spread'] == df['close_spread'].min()].values[0].tolist()
        close_info = close_info[0:2] + close_info[5:]

        logger.info('Open positions info: Difference Coin-Bid1 Spot-Ask1')
        logger.debug(str(open_info))
        logger.info('Close positions info: Difference Coin-Ask1 Spot-Bid1')
        logger.debug(str(close_info))

        print(df.sort_values('open_spread', ascending=False).to_string(index=False))

        return open_info, close_info


if __name__ == '__main__':
    exchange = BA()
    LOGGER = get_logger("Spread Detection")
    while True:
        LOGGER.warning("New round for price detection")
        exchange.get_spread_info(logger=LOGGER)

        time.sleep(exchange.time_interval)
