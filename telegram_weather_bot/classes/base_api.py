import json
import requests


class Base_API():
    def __init__(self):
        pass

    def make_api_call(self, url):
        try:
            res = requests.get(url)
            data = json.loads(res.text)
            return data

        except Exception as e:
            raise e
