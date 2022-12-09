'''
@Description: Parameter Configurations
@Author: Yang Boyu
@Email: bradleyboyuyang@gmail.com
'''

# NOTE: the API should open user universal transfer
BINANCE_CONFIG = {
    'apiKey': '',
    'secret': '',
    'timeout': 3000,
    'rateLimit': 10,
    'verbose': False,
    'hostname': 'binancezh.com', 
    # 'proxies': {'http': 'http://127.0.0.1:7890', 'https': 'https://127.0.0.1:7890'}
    'enableRateLimit': False}

# coin-margin multiplier
# https://www.binance.com/zh-CN/futures/trading-rules/quarterly
multiplier = {
    'BTC': 100,  # 1 contract = 100USD
    'EOS': 10,  # 1 contract = 10USD
    'DOT': 10,
    'ETH': 10,
    'LTC': 10,
    'EOS': 10,
    'XRP': 10,
    'FIL': 10,
    'ADA': 10,
}  


