import unittest
import os

from generic_components.twitter_stream_listener import TwitterStreamListener
from config.log import configure_logging

configure_logging()

consumer_key = os.environ.get('TWITTER_CONSUMER_KEY', None)
consumer_secret = os.environ.get('TWITTER_CONSUMER_SECRET', None)
access_token = os.environ.get('TWITTER_ACCESS_TOKEN_KEY', None)
access_token_secret = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET', None)

class Test(unittest.TestCase):

    #simple sanity test
    def test(self):

        twitter_stream_listener = TwitterStreamListener(consumer_key,
                                                        consumer_secret,
                                                        access_token,
                                                        access_token_secret)

        all_hash_tags = []

        iterations = 20

        for item in twitter_stream_listener.listen("Facebook"):

            hashtags = [tag['text'] for tag in item['entities']['hashtags']]
            all_hash_tags.extend(hashtags)

            if iterations == 0:
                break
            else:
                iterations -= 1

        self.assertGreater(len(all_hash_tags), 0)
