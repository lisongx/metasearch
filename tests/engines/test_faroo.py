import os, unittest
from engines.faroo import FarooEngine


class TestFarooEngine(unittest.TestCase):

    def setUp(self):
        self.engine = FarooEngine(configs={
            "api_key": os.environ["FAROO_API_KEY"]
        })

    def test_request(self):
        results = self.engine.search("python")
        self.assertTrue(isinstance(results, list))

    def test_count(self):
        results = self.engine.search("python", limit=5)
        self.assertEquals(len(results), 5)


if __name__ == '__main__':
    unittest.main()