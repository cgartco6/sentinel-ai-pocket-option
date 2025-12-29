import ccxt
import pandas as pd

exchange = ccxt.binance()

def fetch_ohlc(symbol, timeframe, limit=100):
    data = exchange.fetch_ohlcv(symbol, timeframe, limit=limit)
    df = pd.DataFrame(
        data,
        columns=["time", "open", "high", "low", "close", "volume"]
    )
    return df
