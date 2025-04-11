import requests

def send_telegram_message(message: str) ->None:
    token = "7694966567:AAEpb6K1F3-xMZxdJ-SW-CbuPO6Fos8psq4"
    chat_id = -1002611015753

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message
    }
    requests.post(url, data=payload)