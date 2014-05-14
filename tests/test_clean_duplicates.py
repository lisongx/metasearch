import pytest
from tests import Result, TestEngine


@pytest.fixture(scope="module")
def engine():
    from aggregator import Aggregator
    engine = Aggregator()
    return engine

@pytest.fixture(scope="module")
def raw_results():
    results = []
    
    for i in range(30):
        if i < 1:
            url = u"http://www.baidu.com"
        elif i < 2:
            url = u"http://www.baidu.com/"
        elif i < 5:
            url = u"http://www.google.com/"
        elif i < 10:
            url = u"http://www.bing.com/"
        elif i < 30:
            url = u"http://www.reddit.com/"
        result = Result.new(url, u"test title", u"test desc", source=TestEngine())
        results.append(result)

    return results

def test_result_number(engine, raw_results):
    results = engine._clean_duplicate(raw_results)
    assert len(results) == 4

def test_duplicates_counts(engine, raw_results):
    results = engine._clean_duplicate(raw_results)
    for result in results:
        if result.url == u"http://www.baidu.com/":
            assert result.duplicates == 1
        if result.url == u"http://www.google.com/":
            assert result.duplicates == 2
        if result.url == u"http://www.bing.com/":
            assert result.duplicates == 4
        if result.url ==  u"http://www.reddit.com/":
            assert result.duplicates == 19
    