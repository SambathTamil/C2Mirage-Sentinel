import requests
import json

def send_alert(message):

    # Load Telegram configuration
    with open("config/config.json") as f:
        config = json.load(f)

    token = config["telegram_token"]
    chat_id = config["chat_id"]

    # Telegram API URL
    url = f"https://api.telegram.org/bot{token}/sendMessage"

    payload = {
        "chat_id": chat_id,
        "text": message
    }

    # Send alert
    requests.post(url, data=payload)