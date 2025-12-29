BLOCKED_TIMES = ["12:30", "14:00"]

def news_block(now):
    return now.strftime("%H:%M") in BLOCKED_TIMES
