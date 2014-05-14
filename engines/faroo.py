from .base import RequestEngine,  ResultItemBase

import requests


class FarooEngine(RequestEngine):
    """FAROO is a universal web search engine based on peer-to-peer technology.
       * need init with a api_key
    """
    name = "faroo"
    url = "http://www.faroo.com/"

    DEFAULT_WEIGHT = 0.4
    REQUEST_PATH = "http://www.faroo.com/api"
    RESULT_MAX_LIMIT = 10

    def _send_request(self, query, **kwargs):
        kwargs.update({
            "key": self.api_key,
            "q": query,
            "src": "web",
            "l": kwargs.pop("lang", self.DEFAULT_LANG)
        })

        if "limit" in kwargs:
            kwargs["length"] = kwargs["limit"]
            kwargs.pop("limit")

        r = requests.get(self.REQUEST_PATH, params=kwargs)
        return r.json()

    def _clean_raw_data(self, raw_data):
        results = [FarooResultItem.new(item, source=self) for item in raw_data["results"]]
        return results


class FarooResultItem(ResultItemBase):

    def __init__(self, data):
        self.url = data["url"]
        self.title = data["title"]
        self.image = data["iurl"]
        self.description = data["kwic"]