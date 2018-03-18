# -*- coding: utf-8 -*-
"""
Simple example using BarGraphItem
"""

from TwitterAPI import TwitterAPI
import logging

#override tweepy.StreamListener to add logic to on_status
class TwitterStreamListener():

    def __init__(self, consumer_key, consumer_secret, access_token_key, access_token_secret):
        self.logger = logging.getLogger(TwitterStreamListener.__name__)
        self.api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

    def listen(self, follow_up_sentence):
        return self.api.request('statuses/filter', {'track': follow_up_sentence})

