import csv
from datetime import datetime

def log_trade(symbol, direction, confidence, result):
    with open("ai/trades.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            datetime.utcnow(),
            symbol,
            direction,
            confidence,
            result
        ])
