import requests
import json

from auth import Auth


class Request:
    def __init__(self):
        self.url = "https://oauth.reddit.com/"
        self.header = Auth().main()

    def get(self, endpoint):

        request_url = self.url + endpoint
        response = requests.get(request_url, headers=self.header)

        if response.status_code == 200:
            return json.loads(response.text)
        else:
            raise RuntimeError(response.status_code, response.text)
