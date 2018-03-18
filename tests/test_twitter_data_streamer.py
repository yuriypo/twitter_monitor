import unittest
import os

from generic_components import TwitterStreamListener
from generic_components import TwitterStreamer
from generic_components import HashTagsSummarizer

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

        ITERATION_CLEANUP_FREQUENCY = 10
        HASHTAG_CLEANUP_TTL_SECONDS = 20

        summarizer = HashTagsSummarizer(ITERATION_CLEANUP_FREQUENCY,
                                        HASHTAG_CLEANUP_TTL_SECONDS)

        all_hash_tags = []

        data_streamer = TwitterStreamer(twitter_stream_listener, summarizer)
        counter = 0

        for hash_tags in data_streamer.stream_data("Facebook"):

            all_hash_tags.extend(hash_tags)

            counter += 1
            if counter == 20:
                break

        self.assertTrue(isinstance(all_hash_tags[0][0], str))
        self.assertTrue(isinstance(all_hash_tags[0][1][0], int))
        self.assertTrue(isinstance(all_hash_tags[0][1][1], float))
