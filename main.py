import requests
import time

TOKEN = "8841744903:AAGLRpnTj00af2rj1QLDh2vMfKr2AK6GMYQ"
URL = f"https://api.telegram.org/bot{TOKEN}/"

offset = None

while True:
    res = requests.get(URL + "getUpdates", params={"offset": offset}).json()

    if "result" in res:
        for update in res["result"]:
            offset = update["update_id"] + 1

            if "message" in update:
                chat_id = update["message"]["chat"]["id"]
                text = update["message"].get("text", "")

                requests.post(URL + "sendMessage", data={
                    "chat_id": chat_id,
                    "text": "Bot ishlayapti ✅"
                })

    time.sleep(1)
