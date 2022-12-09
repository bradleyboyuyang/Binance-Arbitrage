'''
@Description: trading source
@Author: Yang Boyu
@Email: bradleyboyuyang@gmail.com
'''

import argparse
import ccxt

from configs.Config import *
from modules.BinanceArb import BinanceArbBot

def init_argparse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--exchange', default=ccxt.binance(BINANCE_CONFIG), help='exchange')
    parser.add_argument('--coin', type=str, default='ada'.upper())
    parser.add_argument('--future_date', type=str, default='221230', help='expiration date')
    parser.add_argument('--coin_precision', type=int, default=5, help="price precision")
    parser.add_argument('--slippage', type=float, default=0.02, help="proportion of coin price")
    parser.add_argument('--multiplier', type=dict, default=multiplier, help='expiration date')

    # commissionRate
    # https://www.binance.com/en/fee/trading
    # BTC-related: 0; 25% off using BNB; BUSD pairs maker: 0
    parser.add_argument('--spot_fee_rate', type=float, default=1/1000)
    parser.add_argument('--contract_fee_rate', type=float, default=1/10000, help="maker: 0.01%, taker: 0.05%")
    parser.add_argument('--max_trial', type=int, default=5, help="number of trials for connection")

    return parser

if __name__ == '__main__':

    # ***open positions***
    position_parser = init_argparse()
    position_parser.add_argument('--amount', type=int, default=20, help="spot trading amount for one iteration")
    position_parser.add_argument('--num_maximum', type=int, default=3, help="maximum execution numbers")
    position_parser.add_argument('-f', '--threshold', type=int, default=0.025, help="opening threshold")
    args = position_parser.parse_args()

    trading_bot = BinanceArbBot(**vars(args))
    trading_bot.open_position()


    # ***close positions***
    # position_parser = init_argparse()
    # position_parser.add_argument('--amount', type=float, default=10, help="number of coins for one iteration")
    # position_parser.add_argument('--num_maximum', type=int, default=3, help="maximum execution numbers")
    # position_parser.add_argument('--threshold', type=int, default=0.0005, help="closing threshold")
    # args = position_parser.parse_args()

    # trading_bot = BinanceArbBot(**vars(args))
    # trading_bot.close_position()


