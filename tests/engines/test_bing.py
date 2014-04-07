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


if __name__ == '__main__':
    unittest.main()