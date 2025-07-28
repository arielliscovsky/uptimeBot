import requests
from datetime import datetime
import pytz

BOT_URL = "https://invbot.onrender.com"

def main():
    now = datetime.now(pytz.timezone("America/Argentina/Buenos_Aires"))
    hour = now.hour

    if 5 <= hour < 8:
        print(f"[{now.strftime('%H:%M')}] Horario de suspensión – NO se envía ping.")
        return

    try:
        response = requests.get(BOT_URL, timeout=10)
        print(f"[{now.strftime('%H:%M')}] Ping enviado. Status: {response.status_code}")
    except Exception as e:
        print(f"[{now.strftime('%H:%M')}] Error enviando ping: {e}")

if __name__ == "__main__":
    main()