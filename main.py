# from twitter import *
from mastodon import *

# from quotesgenerator.main import *
import dotenv as dv
import os
import requests  # Will be replaced
import json  # Will be replaced
import time

dv.load_dotenv()


class Socialbot:
    def __init__(self):
        api_key = "As3XyZ3Xl3IEUqpyUHpa6A==phjO5S4DqLxtFeqk"
        category = "happiness"
        # Mastodon
        mastodon_email = os.getenv("MASTODON_EMAIL")
        mastodon_password = os.getenv("MASTODON_PASSWORD")
        Mastodon.create_app(
            "InspiringQuotes",
            api_base_url="https://mastodon.social",
            to_file="pytooter_clientcred.secret",
        )
        mastodon = Mastodon(
            client_id="pytooter_clientcred.secret",
        )
        mastodon.log_in(
            f"{mastodon_email}",
            f"{mastodon_password}",
            to_file="pytooter_usercred.secret",
        )
        mastodon = Mastodon(access_token="pytooter_usercred.secret")
        # t = Twitter(auth=OAuth(TOKEN, TOKENSECRET, CONSUMERKEY, CONSUMERSECRET))  # Twitter
        # t.statuses.update(status=content)


while True:
    Socialbot()
    time.sleep(3600)
