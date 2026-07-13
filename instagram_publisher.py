import requests
import time


class InstagramPublisher:
    def __init__(self, access_token, ig_user_id):
        self.access_token = access_token
        self.ig_user_id = ig_user_id
        self.base_url = "https://graph.facebook.com/v19.0"

    def create_media_container(self, caption, image_url=None, video_url=None):
        url = f"{self.base_url}/{self.ig_user_id}/media"

        data = {
            "caption": caption,
            "access_token": self.access_token
        }

        if image_url:
            data["image_url"] = image_url

        if video_url:
            data["video_url"] = video_url

        response = requests.post(url, data=data).json()

        if "id" not in response:
            raise Exception(f"Ошибка создания контейнера: {response}")

        return response["id"]

    def wait_video_ready(self, container_id):
        url = f"{self.base_url}/{container_id}"

        while True:
            response = requests.get(url, params={
                "fields": "status_code",
                "access_token": self.access_token
            }).json()

            status = response.get("status_code")

            if status == "FINISHED":
                return

            if status == "ERROR":
                raise Exception("Ошибка обработки видео Instagram")

            time.sleep(3)

    def publish_container(self, container_id):
        url = f"{self.base_url}/{self.ig_user_id}/media_publish"

        response = requests.post(url, data={
            "creation_id": container_id,
            "access_token": self.access_token
        }).json()

        if "id" not in response:
            raise Exception(f"Ошибка публикации: {response}")

        return response["id"]

    def publish_post(self, caption, image_url=None, video_url=None):
        container_id = self.create_media_container(
            caption=caption,
            image_url=image_url,
            video_url=video_url
        )

        if video_url:
            self.wait_video_ready(container_id)

        post_id = self.publish_container(container_id)

        return post_id
