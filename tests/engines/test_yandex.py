import os, unittest
from engines.yandex import YandexEngine


class TestFarooEngine(unittest.TestCase):

    def setUp(self):
        self.engine = YandexEngine(configs={
            "api_key": os.environ["YANDEX_API_KEY"],
            "username": os.environ["YANDEX_USER_NAME"]
        })

    def test_request(self):
        results = self.engine.search("python")
        self.assertTrue(isinstance(results, list))


if __name__ == '__main__':
    unittest.main()