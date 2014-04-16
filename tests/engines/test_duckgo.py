import unittest
from engines import DuckgoEngine


class TestDuckgoEngine(unittest.TestCase):

    def setUp(self):
        self.engine = DuckgoEngine()
        self.results = self.engine.search("python")

    def test_request(self):
        results = self.results
        self.assertTrue(isinstance(results, list))

    def test_result_item(self):
        item = self.results[0]
        self.assertTrue(hasattr(item, "title"))
        self.assertTrue(hasattr(item, "url"))
        self.assertTrue(hasattr(item, "description"))
        self.assertTrue(item.source.name, 'duckduckgo')

    def test_result_priority(self):
        item = self.results[1]
        self.assertEquals(item.priority, 1)


if __name__ == '__main__':
    unittest.main()