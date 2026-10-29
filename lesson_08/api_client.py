import os
import requests
from dotenv import load_dotenv

load_dotenv()


class YougileApi:
    def __init__(self):
        self.base_url = os.getenv(
            "YOUGILE_BASE_URL",
            "https://ru.yougile.com/api-v2")
        self.token = os.getenv("YOUGILE_API_KEY")
        if not self.token:
            raise ValueError(
                "Токен не найден. Установите YOUGILE_API_KEY в .env")

        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

    def create_project(self, title: str, users: dict = None):
        """POST /api-v2/projects"""
        payload = {"title": title}
        if users:
            payload["users"] = users

        return requests.post(
            f"{self.base_url}/projects",
            json=payload,
            headers=self.headers
        )

    def update_project(
            self,
            project_id: str,
            title: str = None,
            deleted: bool = None):
        """PUT /api-v2/projects/{id}"""
        payload = {}
        if title is not None:
            payload["title"] = title
        if deleted is not None:
            payload["deleted"] = deleted

        return requests.put(
            f"{self.base_url}/projects/{project_id}",
            json=payload,
            headers=self.headers
        )

    def get_project(self, project_id: str):
        """GET /api-v2/projects/{id}"""
        return requests.get(
            f"{self.base_url}/projects/{project_id}",
            headers=self.headers
        )
