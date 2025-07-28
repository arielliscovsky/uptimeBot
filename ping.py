import requests
from datetime import datetime
import pytz

RENDER_BOT_URL = "https://invbot.onrender.com"

now = datetime.now(pytz.timezone("America/Argentina/Buenos_Aires"))
if now.hour < 4 or now.hour >= 9:
    try:
        r = requests.get(RENDER_BOT_URL, timeout=10)
        print(f"[{now.strftime('%H:%M')}] Ping success: {r.status_code}")
    except Exception as e:
        print(f"[{now.strftime('%H:%M')}] Ping failed: {e}")
else:
    print(f"[{now.strftime('%H:%M')}] Silent window — no ping sent")