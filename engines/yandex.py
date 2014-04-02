from .base import EngineBase 
from yandexsearch import YaSearch


class YandexEngine(EngineBase):
    """Yandex.
       * need init with a username and api_key
    """

    def __init__(self, configs={}):
        super(YandexEngine, self).__init__(configs)
        self.yasearch = YaSearch(self.username, self.api_key)

    def send_request(self, query, **kwargs):
        return self.yasearch.search(query, **kwargs)

    def clean_raw_data(self, raw_data):
        if raw_data.error is None:
            return raw_data.items
        else:
            raise raw_data.error.description