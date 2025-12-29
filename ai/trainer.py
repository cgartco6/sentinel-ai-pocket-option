"""
SentinelAI Trainer
==================
Purpose:
- Train a probability model for SHORT-TERM breakout signals
- Used for confidence scoring (NOT auto-trading)
- Optimized for 1m–5m expiry logic (Pocket Option style)

Assets:
- BTC
- Forex pairs
- Gold
- Oil

This model DOES NOT trade.
It only outputs probability/confidence.
"""

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import os

# -----------------------------
# CONFIG
# -----------------------------

DATA_PATH = "ai/training_data.csv"
MODEL_PATH = "ai/model.pkl"
MIN_ROWS_REQUIRED = 500   # minimum data to avoid junk models
RANDOM_STATE = 42

# -----------------------------
# FEATURE ENGINEERING
# -----------------------------

def build_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Expected raw columns in CSV:
    - close
    - ema_fast
    - ema_mid
    - ema_slow
    - rsi
    - volume
    - volume_ma
    - atr
    - result  (1 = win, 0 = loss)
    """

    df = df.copy()

    # EMA compression / expansion
    df["ema_gap_fast_mid"] = abs(df["ema_fast"] - df["ema_mid"]) / df["close"]
    df["ema_gap_mid_slow"] = abs(df["ema_mid"] - df["ema_slow"]) / df["close"]

    # Momentum strength
    df["rsi_strength"] = (df["rsi"] - 50).abs()

    # Volume spike ratio
    df["volume_ratio"] = df["volume"] / df["volume_ma"]

    # Volatility normalized
    df["atr_norm"] = df["atr"] / df["close"]

    features = [
        "ema_gap_fast_mid",
        "ema_gap_mid_slow",
        "rsi_strength",
        "volume_ratio",
        "atr_norm"
    ]

    return df[features + ["result"]]


# -----------------------------
# TRAINING FUNCTION
# -----------------------------

def train_model():
    if not os.path.exists(DATA_PATH):
        raise FileNotFoundError(
            f"Training data not found at {DATA_PATH}. "
            "You must log signals before training."
        )

    df = pd.read_csv(DATA_PATH)

    if len(df) < MIN_ROWS_REQUIRED:
        raise ValueError(
            f"Not enough data to train model. "
            f"Have {len(df)}, need at least {MIN_ROWS_REQUIRED}."
        )

    df = build_features(df)

    X = df.drop("result", axis=1)
    y = df["result"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.2,
        random_state=RANDOM_STATE,
        stratify=y
    )

    model = RandomForestClassifier(
        n_estimators=300,
        max_depth=8,
        min_samples_leaf=20,
        random_state=RANDOM_STATE,
        n_jobs=-1
    )

    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)

    print(f"[SentinelAI] Model accuracy: {acc:.2%}")

    joblib.dump(model, MODEL_PATH)
    print(f"[SentinelAI] Model saved to {MODEL_PATH}")


# -----------------------------
# PREDICTION / CONFIDENCE
# -----------------------------

def load_model():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(
            "Model not trained yet. Run trainer.py first."
        )
    return joblib.load(MODEL_PATH)


def confidence_score(feature_dict: dict) -> float:
    """
    Input:
    feature_dict = {
        "ema_gap_fast_mid": float,
        "ema_gap_mid_slow": float,
        "rsi_strength": float,
        "volume_ratio": float,
        "atr_norm": float
    }

    Output:
    Confidence % (0–100)
    """

    model = load_model()

    X = pd.DataFrame([feature_dict])
    prob = model.predict_proba(X)[0][1]

    return round(prob * 100, 2)


# -----------------------------
# CLI ENTRY
# -----------------------------

if __name__ == "__main__":
    train_model()
