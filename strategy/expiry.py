def optimal_expiry(asset, atr):
    if asset in ["EUR/USD", "GBP/USD"]:
        return "1M"
    if asset in ["BTC/USDT", "ETH/USDT"]:
        return "5M" if atr > 1.5 else "2M"
    if asset == "XAUUSD":
        return "3M"
    return "1M"
