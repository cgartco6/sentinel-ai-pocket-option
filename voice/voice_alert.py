from gtts import gTTS
import os

def speak(asset, direction, confidence):
    text = f"{asset.upper()} {direction} signal. Confidence {confidence} percent."
    tts = gTTS(text)
    file = f"voice_{asset}.mp3"
    tts.save(file)
    os.system(f"start {file}" if os.name=="nt" else f"mpg123 {file}")
