import csv, os
from datetime import datetime

BASE = "ai/data"

def log_trade(asset, close, ema_fast, ema_mid, ema_slow, rsi, volume, volume_ma, atr, result):
    path = f"{BASE}/{asset}_training.csv"
    exists = os.path.isfile(path)

    with open(path, "a", newline="") as f:
        writer = csv.writer(f)
        if not exists:
            writer.writerow([
                "timestamp","close","ema_fast","ema_mid","ema_slow",
                "rsi","volume","volume_ma","atr","result"
            ])
        writer.writerow([
            datetime.utcnow().isoformat(),
            close, ema_fast, ema_mid, ema_slow,
            rsi, volume, volume_ma, atr, result
        ])
