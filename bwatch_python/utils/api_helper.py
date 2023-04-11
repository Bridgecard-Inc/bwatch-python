import json
from typing import Optional
import requests
from ..utils.bwatch_data_context import bwatch_python_data_context


class ApiHelper:
    def __init__(self):

        self.headers = {
            "Accept": "application/json",
            # "token": f"Bearer {token}",
            "Content-Type": "application/json",
        }

    def post(self, url: str, data: dict):

        self.headers["token"] = f"Bearer {bwatch_python_data_context.auth_token}"

        response = requests.post(url=url, headers=self.headers, data=json.dumps(data))

        # print(json.loads(response.text))

        if response.status_code == 200:
            return json.loads(response.text)
        else:
            return None

    def delete(self, url: str):

        self.headers["token"] = f"{bwatch_python_data_context.auth_token}"

        response = requests.delete(url=url, headers=self.headers)

        if response.status_code == 200:
            return True
        else:
            return False

    def patch(self, url: str, data: Optional[dict] = {}):

        self.headers["token"] = f"{bwatch_python_data_context.auth_token}"

        response = requests.patch(url=url, headers=self.headers, data=json.dumps(data))

        if response.status_code == 200:
            return True
        else:
            return False
