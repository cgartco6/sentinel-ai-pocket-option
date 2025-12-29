import ta

def apply_indicators(df):
    df["ema9"] = ta.trend.ema_indicator(df["close"], 9)
    df["ema21"] = ta.trend.ema_indicator(df["close"], 21)
    df["rsi"] = ta.momentum.rsi(df["close"], 14)
    df["atr"] = ta.volatility.average_true_range(
        df["high"], df["low"], df["close"], 14
    )
    df["vol_avg"] = df["volume"].rolling(20).mean()
    return df
