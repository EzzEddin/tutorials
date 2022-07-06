import tweepy
import os


def get_api(**kwargs):
    """Gets the API object after authorization
    and authentication.
    :keyword tweepy_api_key: The consumer API key.
    :keyword tweepy_api_key_secret: The consumer API key secret.
    :keyword tweepy_access_token: The access token.
    :keyword tweepy_access_token_secret: The access token secret.
    :returns: The Tweepy API object.
    """
    auth = tweepy.OAuthHandler(
        kwargs["tweepy_api_key"],
        kwargs["tweepy_api_key_secret"]
        )
    auth.set_access_token(
        kwargs["tweepy_access_token"],
        kwargs["tweepy_access_token_secret"]
        )
    return tweepy.API(auth)


api = get_api(
    tweepy_api_key=os.getenv("TWEEPY_API_KEY"),
    tweepy_api_key_secret=os.getenv("TWEEPY_API_KEY_SECRET"),
    tweepy_access_token=os.getenv("TWEEPY_ACCESS_TOKEN"),
    tweepy_access_token_secret=os.getenv("TWEEPY_ACCESS_TOKEN_SECRET")
)
resp = api.get_oembed(
    "https://twitter.com/ButterCMS/status/1521867388882649089"
    )
