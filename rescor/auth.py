import json
from os import path, environ
from dotenv import load_dotenv
import requests
import requests.auth

# Authenticate to the Reddit OAuth2 API
# https://github.com/reddit-archive/reddit/wiki/oauth2


class Auth:
    def __init__(self):
        self.app_dir = path.dirname(path.dirname(__file__))
        load_dotenv("/".join([self.app_dir, ".env"]))

        self.CLIENT_ID = environ.get("CLIENT_ID")
        self.CLIENT_SECRET = environ.get("CLIENT_SECRET")
        self.USERNAME = environ.get("USERNAME")
        self.PASSWORD = environ.get("PASSWORD")

    def main(self):

        client_auth = requests.auth.HTTPBasicAuth(self.CLIENT_ID, self.CLIENT_SECRET)

        post_data = {
            "grant_type": "password",
            "username": self.USERNAME,
            "password": self.PASSWORD,
        }

        headers = {"User-Agent": "rescor0.0.1 by DigSec"}

        auth_response = requests.post(
            url="https://www.reddit.com/api/v1/access_token",
            auth=client_auth,
            data=post_data,
            headers=headers,
        )

        try:
            token = auth_response.json()["access_token"]
            headers["Authorization"] = "bearer {}".format(token)
            return headers

        except:
            print(auth_response.status_code, auth_response.text)


print(Auth().main())
