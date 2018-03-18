import os

ENV_TYPE = os.environ.get("ENV_TYPE", "PROD")

CONSUMER_KEY = os.environ.get('TWITTER_CONSUMER_KEY', None)
CONSUMER_SECRET = os.environ.get('TWITTER_CONSUMER_SECRET', None)
ACCESS_TOKEN = os.environ.get('TWITTER_ACCESS_TOKEN_KEY', None)
ACCESS_TOKEN_SECRET = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET', None)
