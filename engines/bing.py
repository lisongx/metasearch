from .base import EngineBase
from bingsearch import BingSearch


class BingEngine(EngineBase):
    """Bing.
       * need init with a api_key
    """
    def config(self):
        self.bing = BingSearch(self.api_key)

    def _send_request(self, query, **kwargs):
        if "start" in kwargs:
            kwargs["offset"] = kwargs.pop("start")

        return self.bing.search(query, **kwargs)

    def clean_raw_data(self, raw_data):
        return raw_data.results