from .base import EngineBase
from bingsearch import BingSearch


class BingEngine(EngineBase):
    """Bing.
       * need init with a api_key
    """

    # def __init__(self, configs={}):
    #     super(BingEngine, self).__init__(configs)
    #     self.bing = BingSearch(self.api_key)

    def config(self):
        self.bing = BingSearch(self.api_key)

    def send_request(self, query, **kwargs):
        return self.bing.search(query, **kwargs)

    def clean_raw_data(self, raw_data):
        return raw_data.results