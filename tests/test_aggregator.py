import os
import pytest
from engines import BingEngine, DuckgoEngine, FarooEngine, YandexEngine
from engines.base import EngineBase, ResultItemBase
from aggregator import Aggregator


bing = BingEngine(api_key=os.environ["BING_API_KEY"])
duckduckgo = DuckgoEngine()
faroo = FarooEngine(api_key=os.environ["FAROO_API_KEY"])
yandex = YandexEngine(
        api_key=os.environ["YANDEX_API_KEY"],
        username=os.environ["YANDEX_USER_NAME"]
    )

@pytest.fixture(scope="module")
def engine():
    engine = Aggregator
    return engine

@pytest.fixture(scope="module")
def results(engine):
    return engine.search("python")

def test_add(engine):
    engine.add_engine(bing)
    engine.add_engine(duckduckgo)        
    assert len(engine._engines) == 2
    engine._engines = {}

def test_adds(engine):
    engine.add_engines([duckduckgo, yandex, faroo])
    assert len(engine._engines) == 3
    engine._engines = {}

def test_add_fail(engine):
    engine.add_engine(faroo)
    with pytest.raises(Exception):
        engine.add_engine(faroo)
    engine._engines = {}

def test_remove_engine(engine):
    engine.add_engine(faroo)
    engine.remove_engine('faroo')
    assert len(engine._engines) == 0

def test_get_a_single_engine(engine):
    engine.add_engine(faroo)
    assert isinstance(engine['faroo'], EngineBase)
    engine._engines = {}

def test_set_weights(engine):
    engine.add_engines([duckduckgo, yandex, faroo])
    engine.set_weights({
        "duckduckgo": 0.3,
        "yandex": 0.9,
        "faroo": 0.1
    })
    assert engine['duckduckgo'].weight == 0.3
    assert engine['yandex'].weight == 0.9
    assert engine['faroo'].weight == 0.1
    engine._engines = {}