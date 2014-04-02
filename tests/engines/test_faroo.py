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


if __name__ == '__main__':
    unittest.main()