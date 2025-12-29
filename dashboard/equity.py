import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("ai/data/btc_training.csv")
balance = 100
curve = []

for r in df["result"]:
    balance += 0.92 if r==1 else -1
    curve.append(balance)

plt.plot(curve)
plt.title("BTC Equity Curve")
plt.show()
