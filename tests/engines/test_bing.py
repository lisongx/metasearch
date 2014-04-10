import os, unittest
from engines.bing import BingEngine


class TestBingEngine(unittest.TestCase):

    def setUp(self):
        self.engine = BingEngine(configs={
            "api_key": os.environ["BING_API_KEY"]
        })


    def test_request(self):
        results = self.engine.search("python")
        self.assertTrue(isinstance(results, list))

    def test_count(self):
        results = self.engine.search("python", limit=5)
        self.assertEquals(len(results), 5)


if __name__ == '__main__':
    unittest.main()