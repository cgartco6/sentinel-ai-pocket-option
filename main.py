import yaml, time, datetime
from data.market_fetcher import fetch_ohlc
from indicators.indicators import apply_indicators
from strategy.breakout import detect_breakout
from strategy.pocket_filter import pocket_filter
from strategy.mtf import confirm_mtf
from strategy.expiry import optimal_expiry
from ai.confidence import confidence_score
from filters.news import news_block
from telegram.notifier import send_signal

cfg = yaml.safe_load(open("config/settings.yaml"))

while True:
    now = datetime.datetime.utcnow()
    if news_block(now):
        time.sleep(60)
        continue

    for asset in cfg["assets"]["crypto"]:
        df_1m = apply_indicators(fetch_ohlc(asset, "1m"))
        df_5m = apply_indicators(fetch_ohlc(asset, "5m"))

        direction = detect_breakout(df_1m)
        if not direction:
            continue

        if not pocket_filter(df_1m, direction):
            continue

        if not confirm_mtf(df_5m, direction):
            continue

        conf = confidence_score(df_1m, direction)
        if conf < cfg["min_confidence"]:
            continue

        expiry = optimal_expiry(asset, df_1m["atr"].iloc[-1])

        msg = f"""
🚨 SENTINEL AI SIGNAL
Asset: {asset}
Direction: {direction}
Timeframe: 1M
Expiry: {expiry}
Confidence: {conf}%
"""

        send_signal(cfg["telegram"]["bot_token"], cfg["telegram"]["channel_id"], msg)
        send_signal(cfg["telegram"]["bot_token"], cfg["telegram"]["group_id"], msg)

    time.sleep(60)
