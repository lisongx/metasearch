from .base import EngineBase, ResultItemBase
from yandexsearch import YaSearch


class YandexEngine(EngineBase):
    """Yandex.
       * need init with a username and api_key
    """
    name = "yandex"
    weight = 0.3
    url = "http://www.yandex.com/"

    def _post_config(self):
        self.yasearch = YaSearch(self.username, self.api_key)

    def _send_request(self, query, **kwargs):
        return self.yasearch.search(query, **kwargs)

    def _clean_raw_data(self, raw_data):
        if raw_data.error is None:
            results = [YandexResultItem.new(item) for item in raw_data.items]
            return results
        else:
            return []


class YandexResultItem(ResultItemBase):

    source = YandexEngine

    def __init__(self, data):
        self.url = data.url
        self.title = data.title
        self.description = data.snippet
        self.image = None