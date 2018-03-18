import sys
import argparse
import signal, os
import logging
import time

from config.log import configure_logging
configure_logging()

from ioc.ioc_manager import get_twitter_follow_up_monitor

parser = argparse.ArgumentParser(description='Follow up sentence from Twitter.')
parser.add_argument('--sentence', type=str,required=True, help='Sentence to follow up')

# App entry point
def main():
    parser.parse_args(sys.argv[1:])

    follow_up_sentence = parser.parse_args(sys.argv[1:]).sentence

    logging.getLogger("").info("Starting twitter monitoring for sentecne " + follow_up_sentence)

    monitor = get_twitter_follow_up_monitor()

    # Process exit handling.
    def sig_handler(sig):
        logging.getLogger("SigHandler").info('%s Caught signal: %s Exiting.', os.getpid(), sig)
        monitor.close()
        sys.exit(0)

    signal.signal(signal.SIGTERM, lambda sig, frame: sig_handler(sig))
    signal.signal(signal.SIGINT, lambda sig, frame: sig_handler(sig))

    monitor.follow_up(follow_up_sentence)

if __name__== "__main__":
  main()


