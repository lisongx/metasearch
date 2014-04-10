import os, unittest
from engines.yandex import YandexEngine


class TestFarooEngine(unittest.TestCase):

    def setUp(self):
        self.engine = YandexEngine(configs={
            "api_key": os.environ["YANDEX_API_KEY"],
            "username": os.environ["YANDEX_USER_NAME"]
        })
        self.results = self.engine.search("python")

    def test_request(self):
        results = self.results
        self.assertTrue(isinstance(results, list))

    def test_result_item(self):
        item = self.results[0]
        self.assertTrue(hasattr(item, "title"))
        self.assertTrue(hasattr(item, "url"))
        self.assertTrue(hasattr(item, "description"))        


if __name__ == '__main__':
    unittest.main()