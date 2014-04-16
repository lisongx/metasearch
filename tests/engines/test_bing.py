import os, unittest
from engines import BingEngine


class TestBingEngine(unittest.TestCase):

    def setUp(self):
        self.engine = BingEngine(api_key=os.environ["BING_API_KEY"])
        self.results = self.engine.search("python")

    def test_request(self):
        results = self.results
        self.assertTrue(isinstance(results, list))

    def test_result_item(self):
        item = self.results[0]
        self.assertTrue(hasattr(item, "title"))
        self.assertTrue(hasattr(item, "url"))
        self.assertTrue(hasattr(item, "description"))        
        self.assertTrue(item.source.name, 'bing')

    def test_result_priority(self):
        item = self.results[2]
        self.assertEquals(item.priority, 2)

    def test_count(self):
        results = self.engine.search("python", limit=5)
        self.assertEquals(len(results), 5)


if __name__ == '__main__':
    unittest.main()