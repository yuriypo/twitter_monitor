from config.log import configure_logging
from config.env import ACCESS_TOKEN, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET

from generic_components import \
    TwitterStreamListener, \
    HashTagsSummarizer, \
    TwitterStreamer, \
    GraphPresentor, \
    TwitterFollowUpMonitor

# Module responsible for all objects instantiation.
configure_logging()

def get_twitter_stream_listener():
    return TwitterStreamListener(CONSUMER_KEY,
                                 CONSUMER_SECRET,
                                 ACCESS_TOKEN,
                                 ACCESS_TOKEN_SECRET)

def get_hash_tags_summarizer():
    ITERATION_CLEANUP_FREQUENCY = 20
    HASHTAG_CLEANUP_TTL_SECONDS = 120

    return HashTagsSummarizer(ITERATION_CLEANUP_FREQUENCY, HASHTAG_CLEANUP_TTL_SECONDS)

def get_twitter_streamer():
    return TwitterStreamer(get_twitter_stream_listener(), get_hash_tags_summarizer())

def get_graph_presentor():
    return GraphPresentor()

def get_twitter_follow_up_monitor():
    return TwitterFollowUpMonitor(get_twitter_streamer(), get_graph_presentor())
