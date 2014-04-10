from .base import RequestEngine

import requests


class FarooEngine(RequestEngine):
    """FAROO is a universal web search engine based on peer-to-peer technology.
       * need init with a api_key
    """

    REQUEST_PATH = "http://www.faroo.com/api"

    def send_request(self, query, **kwargs):
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

    def clean_raw_data(self, raw_data):
        return raw_data["results"]