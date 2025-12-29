import csv
import os
from datetime import datetime

DATA_DIR = "ai/data"

os.makedirs(DATA_DIR, exist_ok=True)

def log_trade(
    asset: str,
    close: float,
    ema_fast: float,
    ema_mid: float,
    ema_slow: float,
    rsi: float,
    volume: float,
    volume_ma: float,
    atr: float,
    result: int
):
    file_path = f"{DATA_DIR}/{asset.lower()}_training.csv"

    file_exists = os.path.isfile(file_path)

    with open(file_path, "a", newline="") as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow([
                "timestamp",
                "close",
                "ema_fast",
                "ema_mid",
                "ema_slow",
                "rsi",
                "volume",
                "volume_ma",
                "atr",
                "result"
            ])

        writer.writerow([
            datetime.utcnow().isoformat(),
            close,
            ema_fast,
            ema_mid,
            ema_slow,
            rsi,
            volume,
            volume_ma,
            atr,
            result
        ])
