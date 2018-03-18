# -*- coding: utf-8 -*-


import logging
import time

class HashTagsSummarizer():
    """
    Component responsibility is to summarize hash_tags.
    stores hashtags in lookup table ("HashTags") -> (count , update_time)
    """

    MAX_TOP_HASHTAGS_TO_KEEP = 100
    DEFAUL_CLEAN_UP_FREQUENCY = 100
    DEFAUL_CLEAN_UP_TTL = 60 * 60 * 24 *7

    def __init__(self, clean_up_frequency, clean_up_ttl=None, max_top_hash_tags_to_keep=None):
        self.logger = logging.getLogger(HashTagsSummarizer.__name__)
        self.hash_tags_lookup = {}
        self.consume_counter = 0
        self.clean_up_frequency = clean_up_frequency if clean_up_frequency > 0 \
            else HashTagsSummarizer.DEFAUL_CLEAN_UP_FREQUENCY

        self.clean_up_ttl = clean_up_ttl
        if self.clean_up_ttl is None:
            self.clean_up_ttl = HashTagsSummarizer.DEFAUL_CLEAN_UP_TTL

        self.max_top_hash_tags_to_keep = max_top_hash_tags_to_keep
        if self.max_top_hash_tags_to_keep is None:
            self.clean_up_ttl = HashTagsSummarizer.MAX_TOP_HASHTAGS_TO_KEEP

    # returns hashtags sorted by appearance count, desc
    def get_top_hash_tags(self, count):
        return sorted(self.hash_tags_lookup.items(), key=lambda x: x[1][0], reverse=True)[0:count]


    def consume_hashtags(self, hashtags):
        self.consume_counter += 1
        if self.consume_counter == self.clean_up_frequency:
            self.clean_up_procedure()
            self.consume_counter = 0

        for hashtag in hashtags:
            hashtag = hashtag.lower().strip()
            self.hash_tags_lookup[hashtag] = (self.hash_tags_lookup.get(hashtag, (0, 0))[0] + 1, time.time())

    def clean_up_procedure(self):
        to_clean_up = sorted(self.hash_tags_lookup.items(),\
                             key=lambda x: x[1][1],reverse=True)[self.max_top_hash_tags_to_keep:]
        cleaned = 0
        for hashtag, count in to_clean_up:
            if time.time() - count[1] > self.clean_up_ttl:
                self.hash_tags_lookup.pop(hashtag)
                cleaned += 1

        self.logger.info("Cleaning %d hashtags." % (cleaned))
        self.logger.info("Remaining %d hashtags : %s" % (len(self.hash_tags_lookup), str(self.hash_tags_lookup)))
