def confirm_mtf(df_5m, direction):
    if direction == "BUY":
        return df_5m["ema9"].iloc[-1] > df_5m["ema21"].iloc[-1]
    if direction == "SELL":
        return df_5m["ema9"].iloc[-1] < df_5m["ema21"].iloc[-1]
    return False
