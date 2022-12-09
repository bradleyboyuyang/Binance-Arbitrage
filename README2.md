# Binance Arbitrage


## 1. 
1. 开多仓：Spot账户买币
2. 万向划转：Spot账户转币至COIN-M账户
3. 开空仓：COIN-M账户做空对应数量币


## Scripts

- `basis_trading.py`：套利开仓平仓主程序
- `configs`：配置集合
  - `Config.py`：超参数定义（账户信息等）
- `modules`：交易所集合
  - `BinanceArb.py`：币安套利大类
- `utils`：工具函数集合
  - `Logger.py`：日志配置
  - `Notifier.py`：异常通知
- `basis_trading.xlsx`：期现套利多空持仓计算表

## 3. 注意事项
1. 用户开启万向划转权限
2. [币本位合约乘数](https://www.binance.com/zh-CN/futures/trading-rules/quarterly)
3. [现货与合约交易手续费](https://www.binance.com/en/fee/trading)
4. 机器人信息Webhook配置加签
5. 下单方式：`TimeInForce`参数（GTC, IOC, FOK, GTX)
6. <font color='blue'>币本位下单与万向划转的顺序</font>
7. 防各类网络通讯障碍的容错处理