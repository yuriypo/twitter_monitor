# -*- coding: utf-8 -*-


from TwitterAPI import TwitterAPI
import logging

class TwitterStreamListener():
    """
    Component is reponsible bringing data from twitter solely.
    """
    def __init__(self, consumer_key, consumer_secret, access_token_key, access_token_secret):
        self.logger = logging.getLogger(TwitterStreamListener.__name__)
        self.api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

    def listen(self, follow_up_sentence):
        return self.api.request('statuses/filter', {'track': follow_up_sentence})

