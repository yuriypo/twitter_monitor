import threading
from config.log import configure_logging

configure_logging()

class TwitterFollowUpMonitor():
    def __init__(self, data_streamer, graph):
        self.data_streamer = data_streamer
        self.graph = graph
        self.is_running = True

    def follow_up(self, follow_up_sentence):

        def thread_function(run_indicator):
            if not run_indicator:
                raise Exception("Run indicator required.")

            for hash_tags in self.data_streamer.stream_data(follow_up_sentence):
                if run_indicator.is_running is False:
                    return
                self.graph.update(hash_tags)

        self.thread = threading.Thread(target=thread_function, args=[self])
        self.thread.start()
        self.graph.present()
        self.thread.join()

    def close(self):
        self.is_running = False
        self.graph.stop()










