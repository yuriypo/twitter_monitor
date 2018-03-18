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

def main():
    parser.parse_args(sys.argv[1:])

    follow_up_sentence = parser.parse_args(sys.argv[1:]).sentence

    monitor = get_twitter_follow_up_monitor()

    def sig_handler(sig):
        logging.getLogger("SigHandler").info('%s Caught signal: %s Exiting', os.getpid(), sig)
        monitor.close()
        time.sleep(2)
        sys.exit(0)

    signal.signal(signal.SIGTERM, lambda sig, frame: sig_handler(sig))
    signal.signal(signal.SIGINT, lambda sig, frame: sig_handler(sig))

    monitor.follow_up(follow_up_sentence)

if __name__== "__main__":
  main()


