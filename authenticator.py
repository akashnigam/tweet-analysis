import app_credentials
from tweepy import OAuthHandler


class Authenticator:

    def __init__(self):
        self.auth = OAuthHandler(app_credentials.CONSUMER_KEY, app_credentials.CONSUMER_SECRET)
        self.auth.access_token = app_credentials.ACCESS_TOKEN
        self.auth.access_token_secret = app_credentials.ACCESS_SECRET

    def get_auth(self):
        return self.auth