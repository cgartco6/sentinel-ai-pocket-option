from flask import Flask
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():
    try:
        df = pd.read_csv("ai/trades.csv")
        winrate = (df["result"] == "WIN").mean() * 100
    except:
        winrate = 0
    return f"<h1>SentinelAI</h1><p>Winrate: {winrate:.2f}%</p>"

app.run(port=5000)
