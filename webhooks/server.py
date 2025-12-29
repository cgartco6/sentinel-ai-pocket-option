from flask import Flask, request
from telegram.notifier import send_signal
import yaml

app = Flask(__name__)
cfg = yaml.safe_load(open("config/settings.yaml"))

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    send_signal(
        cfg["telegram"]["bot_token"],
        cfg["telegram"]["channel_id"],
        f"📡 TV SIGNAL\n{data}"
    )
    return {"status": "ok"}

app.run(port=9000)
