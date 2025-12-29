import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def walk_forward_validate(csv_path, window=300):
    df = pd.read_csv(csv_path)

    features = [
        "ema_gap_fast_mid",
        "ema_gap_mid_slow",
        "rsi_strength",
        "volume_ratio",
        "atr_norm"
    ]

    accuracies = []

    for i in range(window, len(df) - 50, 50):
        train = df.iloc[i-window:i]
        test = df.iloc[i:i+50]

        X_train = train[features]
        y_train = train["result"]

        X_test = test[features]
        y_test = test["result"]

        model = RandomForestClassifier(
            n_estimators=200,
            max_depth=8,
            min_samples_leaf=20
        )

        model.fit(X_train, y_train)
        preds = model.predict(X_test)

        acc = accuracy_score(y_test, preds)
        accuracies.append(acc)

    print("Walk-forward accuracy:", round(sum(accuracies)/len(accuracies)*100, 2), "%")
