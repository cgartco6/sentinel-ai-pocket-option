import joblib
import os

MODEL_PATH = "ai/model.pkl"

def confidence_score(df, direction):
    score = 0

    if abs(df["ema9"].iloc[-1] - df["ema21"].iloc[-1]) > df["atr"].iloc[-1]:
        score += 30

    if df["volume"].iloc[-1] > df["vol_avg"].iloc[-1] * 1.8:
        score += 30

    if direction == "BUY" and df["rsi"].iloc[-1] > 60:
        score += 20

    if direction == "SELL" and df["rsi"].iloc[-1] < 40:
        score += 20

    if os.path.exists(MODEL_PATH):
        model = joblib.load(MODEL_PATH)
        score += int(model.predict_proba([[score]])[0][1] * 20)

    return min(score, 100)
