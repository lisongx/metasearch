import os, unittest
from engines import YandexEngine


class TestYandexEngine(unittest.TestCase):

    def setUp(self):
        self.engine = YandexEngine(
            api_key=os.environ["YANDEX_API_KEY"],
            username=os.environ["YANDEX_USER_NAME"]
        )
        self.results = self.engine.search("python")

    def test_request(self):
        results = self.results
        self.assertTrue(isinstance(results, list))

    def test_result_item(self):
        item = self.results[0]
        self.assertTrue(hasattr(item, "title"))
        self.assertTrue(hasattr(item, "url"))
        self.assertTrue(hasattr(item, "description"))
        self.assertTrue(item.source.name, 'yandex')

    def test_result_priority(self):
        item = self.results[3]
        self.assertEquals(item.priority, 3)


if __name__ == '__main__':
    unittest.main()