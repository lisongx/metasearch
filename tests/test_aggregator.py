import os, unittest
from engines import BingEngine, DuckgoEngine, FarooEngine, YandexEngine
from engines.base import ResultItemBase
from aggregator import Aggregator

bing = BingEngine(api_key=os.environ["BING_API_KEY"])
duckduckgo = DuckgoEngine()
faroo = FarooEngine(api_key=os.environ["FAROO_API_KEY"])
yandex = YandexEngine(
        api_key=os.environ["YANDEX_API_KEY"],
        username=os.environ["YANDEX_USER_NAME"]
    )


class TestFarooEngine(unittest.TestCase):

    def setUp(self):
        self.engine = Aggregator()

    def test_add(self):
        self.engine.add_engine(bing)
        self.engine.add_engine(duckduckgo)        
        self.assertEquals(len(self.engine._engines), 2)

    def test_add_fail(self):
        self.engine.add_engine(faroo)
        self.assertRaises(Exception, self.engine.add_engine, faroo)

    def test_remove_engine(self):
        self.engine.add_engine(faroo)
        self.engine.remove_engine('faroo')
        self.assertEquals(len(self.engine._engines), 0)

    def test_search(self):
        self.engine.add_engines([duckduckgo, yandex, faroo])
        results = self.engine.search("python")
        self.assertTrue(isinstance(results[0][0], ResultItemBase))

    def tearDown(self):
        self.engine._engines = []


if __name__ == '__main__':
    unittest.main()