import pandas as pd, joblib, os
from sklearn.ensemble import RandomForestClassifier

DATA = "ai/data/{asset}_training.csv"
MODEL = "ai/models/{asset}.pkl"

def train(asset):
    data = DATA.format(asset=asset)
    model = MODEL.format(asset=asset)

    df = pd.read_csv(data)

    df["ema_gap_fast_mid"] = abs(df["ema_fast"]-df["ema_mid"])/df["close"]
    df["ema_gap_mid_slow"] = abs(df["ema_mid"]-df["ema_slow"])/df["close"]
    df["rsi_strength"] = abs(df["rsi"]-50)
    df["volume_ratio"] = df["volume"]/df["volume_ma"]
    df["atr_norm"] = df["atr"]/df["close"]

    X = df[[
        "ema_gap_fast_mid","ema_gap_mid_slow",
        "rsi_strength","volume_ratio","atr_norm"
    ]]
    y = df["result"]

    clf = RandomForestClassifier(n_estimators=300, max_depth=8)
    clf.fit(X, y)

    joblib.dump(clf, model)
    print(f"{asset.upper()} model trained → {model}")

if __name__ == "__main__":
    for a in ["btc","forex","gold","oil"]:
        train(a)
