confidence = 75

def adjust(win):
    global confidence
    if win:
        confidence = min(confidence+1, 85)
    else:
        confidence = max(confidence-2, 65)
    return confidence
