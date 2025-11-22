import requests

class Client:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def send_log(self, payload):
        return requests.post(f"{self.base_url}/api/logs", json=payload)
