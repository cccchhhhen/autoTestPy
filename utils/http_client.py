import requests
from config.settings import BASE_URL

class HttpClient:
    def post(self, endpoint, data):
        url = f"{BASE_URL}{endpoint}"
        try:
            return requests.post(url, json=data, timeout=5)
        except requests.exceptions.Timeout:
            print("请求超时！")