from .base import RequestEngine,  ResultItemBase

import requests


class FarooEngine(RequestEngine):
    """FAROO is a universal web search engine based on peer-to-peer technology.
       * need init with a api_key
    """

    REQUEST_PATH = "http://www.faroo.com/api"

    def _send_request(self, query, **kwargs):
        kwargs.update({
            "key": self.api_key,
            "q": query,
            "src": "web"
        })

        if "limit" in kwargs:
            kwargs["length"] = kwargs["limit"]
            kwargs.pop("limit")

        r = requests.get(self.REQUEST_PATH, params=kwargs)
        return r.json()

    def _clean_raw_data(self, raw_data):
        results = [FarooResultItem(item) for item in raw_data["results"]]
        return results


class FarooResultItem(ResultItemBase):
    source = "faroo"

    def __init__(self, data):
        self.url = data["url"]
        self.title = data["title"]
        self.image = data["iurl"]
        self.description = data["kwic"]