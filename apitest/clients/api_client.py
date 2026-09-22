import logging

import requests
from requests.exceptions import RequestException

logger = logging.getLogger(__name__)  

class ApiClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        self.token = None

    def request(self, method, url):
        return self.session.request(method, url)

    def login(self, username, password):
        try:
            resp = self.session.post(f"{self.base_url}/api/login",
                                    json={"username":username, "password":password},
                                    )
        except RequestException as e:
            logger.error(f"网络异常: {e}")
            raise
        resp.raise_for_status()
        token = resp.json()["token"]
        self.session.headers.update(
            {"Authorization": f"Bearer {token}"}
        )
        self.token = token
        return resp.json()


    def get_users(self):
        try:
            resp = self.session.get(f"{self.base_url}/api/users")
        except RequestException as e:
            logger.error(f"网络异常: {e}")
            raise
        return resp.json()