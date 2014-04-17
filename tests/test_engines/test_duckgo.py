import pytest

from engines import DuckgoEngine


@pytest.fixture(scope="module")
def engine():
    engine = DuckgoEngine()
    return engine

@pytest.fixture(scope="module")
def results(engine):
    return engine.search("python")

def test_request(results):
    assert isinstance(results, list)

def test_result_item(results):
    item = results[0]
    assert hasattr(item, "title")
    assert hasattr(item, "url")
    assert hasattr(item, "description")
    assert item.source.name == 'duckduckgo'

def test_result_priority(results):
    item = results[1]
    assert item.priority == 1