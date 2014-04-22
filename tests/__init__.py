from engines.base import EngineBase, ResultItemBase


class TestEngine(EngineBase):
    """Bing.
       * need init with a api_key
    """
    name = "Test"
    # weight = 1.0

    def _send_request(self, query, **kwargs):
        pass


class Result(ResultItemBase):
    source = TestEngine

    def __init__(self, url, title, description, weight=5):
        self.url = url
        self.title = title
        self.description = description