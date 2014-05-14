import pytest
from tests import Result, TestEngine

@pytest.fixture(scope="module")
def engine():
    from aggregator import Aggregator
    engine = Aggregator()
    return engine

@pytest.fixture(scope="module")
def results():

    results = []

    for i in range(30):
        url = u"http://www.google.com/%d" % i
        result = Result.new(url, u"test title %d" % i, u"test desc", source=TestEngine())
        result.priority = i % 15
        result.source.weight  = i % 10
        result.duplicates  =  i % 5
        results.append(result)

    return results

def test_result_order(engine, results):
    
    print results