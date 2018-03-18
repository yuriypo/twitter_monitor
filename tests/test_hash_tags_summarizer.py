import unittest
import time
from generic_components.hash_tags_summarizer import HashTagsSummarizer
from config.log import configure_logging

configure_logging()

class Test(unittest.TestCase):

    #simple sanity test
    def test(self):

        ITERATION_CLEANUP_FREQUENCY = 5
        HASHTAG_CLEANUP_TTL_SECONDS = 4
        MAX_TOP_HASHTAGS_TO_KEEP = 2

        summarizer = HashTagsSummarizer(ITERATION_CLEANUP_FREQUENCY,
                                        HASHTAG_CLEANUP_TTL_SECONDS,
                                        MAX_TOP_HASHTAGS_TO_KEEP)

        tags_to_be_removed = ["ToRemove", "ToRemove2"]

        hash_tags = [tags_to_be_removed,
                     ["a", "A ", "a ", "A", "b", "B "],
                     ["a", "A ", "a ", "A", "b", "B "],
                     ["a", "A ", "a ", "A", "b", "B "],
                     ["a", "A ", "a ", "A", "b", "B "],
                     ["a", "A ", "a ", "A", "b", "B "]]

        for iteration_hashtags in hash_tags:
            time.sleep(1)
            summarizer.consume_hashtags(iteration_hashtags)

        top_hash_tags = summarizer.get_top_hash_tags(10)

        self.assertEqual(len(top_hash_tags), 2)
        # value
        self.assertEqual(top_hash_tags[0][0], "a")
        self.assertEqual(top_hash_tags[1][0], "b")
        # count
        self.assertEqual(top_hash_tags[0][1][0], 20)
        self.assertEqual(top_hash_tags[1][1][0], 10)
