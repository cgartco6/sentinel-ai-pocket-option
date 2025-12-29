def pocket_filter(df, direction):
    last = df.iloc[-1]
    body = abs(last["close"] - last["open"])
    wick = abs(last["high"] - last["low"]) - body

    if wick > body * 1.5:
        return False

    if direction == "BUY" and last["close"] < last["open"]:
        return False

    if direction == "SELL" and last["close"] > last["open"]:
        return False

    return True
