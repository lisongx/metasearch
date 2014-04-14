import unittest
from engines import DuckgoEngine


class TestDuckgoEngine(unittest.TestCase):

    def setUp(self):
        self.engine = DuckgoEngine()

    def test_request(self):
        results = self.engine.search("python")
        self.assertTrue(isinstance(results, list))


if __name__ == '__main__':
    unittest.main()