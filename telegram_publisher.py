# posts/telegram_publisher.py
import requests

class TelegramPublisher:
    def __init__(self, bot_token):
        self.bot_token = bot_token

    def send_text(self, text, chat_id):
        url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"
        requests.post(url, data={
            "chat_id": chat_id,
            "text": text
        })

    def send_photo_file(self, photo_file, caption, chat_id):
        url = f"https://api.telegram.org/bot{self.bot_token}/sendPhoto"

        files = {
            "photo": photo_file
        }

        data = {
            "chat_id": chat_id,
            "caption": caption or ""
        }

        response = requests.post(url, files=files, data=data)
        result = response.json()

        if not result.get("ok"):
            raise Exception(result.get("description"))
