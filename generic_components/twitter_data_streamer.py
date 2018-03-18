# -*- coding: utf-8 -*-
"""
Simple example using BarGraphItem
"""

import logging

class TwitterStreamer():

    TOP_HASH_TAGS_NUMBER_TO_RETURN = 10

    def __init__(self, twitter_stream_listener, hash_tags_summarizer, top_hash_tags_to_return=None):
        self.logger = logging.getLogger(TwitterStreamer.__name__)
        self.twitter_stream_listener = twitter_stream_listener
        self.hash_tags_summarizer = hash_tags_summarizer

        self.top_hash_tags_to_return = int(top_hash_tags_to_return) if top_hash_tags_to_return is not None else None
        if self.top_hash_tags_to_return is None:
            self.top_hash_tags_to_return = TwitterStreamer.TOP_HASH_TAGS_NUMBER_TO_RETURN

    def stream_data(self, follow_up_sentence):
        for item in self.twitter_stream_listener.listen(follow_up_sentence):
            if 'entities' not in item:
                continue

            hash_tags = [tag['text'] for tag in item['entities']['hashtags']]
            self.hash_tags_summarizer.consume_hashtags(hash_tags)
            yield self.hash_tags_summarizer.get_top_hash_tags(10)
