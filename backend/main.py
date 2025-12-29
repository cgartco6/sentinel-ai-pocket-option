from backend.signals.engine import generate_signal
from backend.filters.news import news_block

def run():
    asset = "btc"

    if news_block(asset):
        print("Trade blocked by news filter")
        return

    features = {
        "ema_gap_fast_mid": 0.0012,
        "ema_gap_mid_slow": 0.0010,
        "rsi_strength": 12,
        "volume_ratio": 1.8,
        "atr_norm": 0.003
    }

    signal, confidence = generate_signal(asset, features)
    print(f"{asset.upper()} → {signal} ({confidence}%)")

if __name__ == "__main__":
    run()
