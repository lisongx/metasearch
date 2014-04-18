from .base import EngineBase, ResultItemBase
from bingsearch import BingSearch


class BingEngine(EngineBase):
    """Bing.
       * need init with a api_key
    """
    name = "bing"

    def _post_config(self):
        self.bing = BingSearch(self.api_key)

    def _send_request(self, query, **kwargs):
        if "start" in kwargs:
            kwargs["offset"] = kwargs.pop("start")

        return self.bing.search(query, **kwargs)

    def _clean_raw_data(self, raw_data):
        results = [BingResultItem.new(item) for item in raw_data.results]
        return results


class BingResultItem(ResultItemBase):

    source = BingEngine

    def __init__(self, data):
        self.url = data.url
        self.title = data.title
        self.description = data.description
        self.image = None