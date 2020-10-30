import pyupbit

ticker = ["KRW-BTC", "KRW-ETH", "KRW-BCH", "KRW-XRP", "KRW-LTC", "KRW-ETC", "KRW-QTUM", "KRW-ADA", "KRW-NEO", "KRW-EOS", "KRW-TRX", "KRW-BSV", "KRW-BTG"]

print("=====================")

for i in ticker:
    data = pyupbit.get_ohlcv(i)
    live_price = pyupbit.get_current_price(i)
    close_avg = data['close'].tail(5).mean()

    if live_price > close_avg:
        print(f'{i.split("-")[1]} 현재가: {int(live_price):,}원')
        print(f"종가 이동 평균: {int(close_avg):,}원")
        print(i.split("-")[1] + " 상승장!")
        print("=====================")
    else:
        print(f'{i.split("-")[1]} 현재가: {int(live_price):,}원')
        print(f"종가 이동 평균: {int(close_avg):,}원")
        print(i.split("-")[1] + " 하락장!")
        print("=====================")