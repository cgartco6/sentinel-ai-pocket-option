def detect_breakout(df):
    last = df.iloc[-1]
    prev = df.iloc[-2]

    if (
        last["close"] > prev["high"]
        and last["ema9"] > last["ema21"]
        and last["volume"] > last["vol_avg"] * 1.5
        and 55 < last["rsi"] < 70
    ):
        return "BUY"

    if (
        last["close"] < prev["low"]
        and last["ema9"] < last["ema21"]
        and last["volume"] > last["vol_avg"] * 1.5
        and 30 < last["rsi"] < 45
    ):
        return "SELL"

    return None
