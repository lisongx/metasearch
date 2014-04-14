import os, unittest
from engines import FarooEngine


class TestFarooEngine(unittest.TestCase):

    def setUp(self):
        self.engine = FarooEngine(configs={
            "api_key": os.environ["FAROO_API_KEY"]
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
        self.assertTrue(item.source, 'faroo')

    def test_result_priority(self):
        item = self.results[1]
        self.assertEquals(item.priority, 1)

    def test_count(self):
        results = self.engine.search("python", limit=5)
        self.assertEquals(len(results), 5)


if __name__ == '__main__':
    unittest.main()