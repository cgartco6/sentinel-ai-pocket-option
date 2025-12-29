import joblib
import pandas as pd

MODELS = {
    "btc": "ai/models/btc.pkl",
    "forex": "ai/models/forex.pkl",
    "gold": "ai/models/gold.pkl",
    "oil": "ai/models/oil.pkl",
}

def generate_signal(asset, features):
    model = joblib.load(MODELS[asset])
    df = pd.DataFrame([features])
    prob = model.predict_proba(df)[0][1]

    if prob > 0.75:
        return "BUY", round(prob * 100, 2)
    elif prob < 0.25:
        return "SELL", round((1 - prob) * 100, 2)

    return "HOLD", round(prob * 100, 2)
