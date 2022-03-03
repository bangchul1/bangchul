import pyupbit
import time



access = "VtcpyVzbzT7kQsFaRaCzxQS399SK1GRo0gkBI2xN"
secret = "TIYYQ7rG75LzfbJqWrKAcdP3ftToqUNiqxVEKFoE"



# 15시간 이동평균 조회
def get_ma_15h(ticker):
    df = pyupbit.get_ohlcv("KRW-BTC", interval="minute60", count=60)
    close = df['close']
    ma_15h = close.rolling(50).mean().iloc[-2]
    return ma_15h


# 전시간 종가 조회
def get_close(ticker):
    df = pyupbit.get_ohlcv("KRW-BTC", interval="minute60", count=1)
    close = df.iloc[-2]['close']
    return close




# 로그인
upbit =  pyupbit.Upbit(access, secret)

# 자동매매
while True:     
      ma_15h = get_ma_15h("KRW-BTC")
      close = get_close("KRW-BTC")
        
      if ma_15h < close :
         krw = float(upbit.get_balances("KRW"))
         upbit.buy_market_order("KRW-BTC", krw*0.9995)
         
      else:
         btc = float(upbit.get_balances("KRW-BTC"))
         upbit.sell_market_order("KRW-BTC", btc*0.9995)
         
         
         
      time.sleep(60)
