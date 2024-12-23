from mastodon import Mastodon
import dotenv as dv
import os
from quotesgeneratorapi_wrapper.quotesgenerator import getQuotes

dv.load_dotenv()


class Socialbot:
    def __init__(self):
        api_key = os.getenv("APININJASKEY")
        category = "happiness"
        content = getQuotes(category=category, api_key=api_key)
        print(content)
        # Mastodon
        CLIENTKEY = os.getenv("CLIENTKEY")
        CLIENTSECRET = os.getenv("CLIENTSECRET")
        ACCESSTOKEN = os.getenv("ACCESSTOKEN")
        mastodon = Mastodon(
            client_id=CLIENTKEY,
            client_secret=CLIENTSECRET,
            access_token=ACCESSTOKEN,
            api_base_url="https://mastodon.social",
        )
        mastodon.toot(content)


if __name__ == "__main__":
    Socialbot()
