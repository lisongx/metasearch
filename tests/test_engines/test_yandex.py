# -*- coding: utf-8 -*-

import os
import pytest
from engines import YandexEngine

@pytest.fixture(scope="module")
def engine():
    engine = YandexEngine(
        api_key=os.environ["YANDEX_API_KEY"],
        username=os.environ["YANDEX_USER_NAME"]
    )
    return engine

@pytest.fixture(scope="module")
def results(engine):
    return engine.search("python")

@pytest.fixture(scope="module")
def chinese_results(engine):
    return engine.search(u"豆瓣")

def test_results_is_list(results):
    assert isinstance(results, list)

def test_chinese_request(chinese_results):
    assert isinstance(chinese_results, list)

def test_result_item(results):
    item = results[0]
    assert hasattr(item, "title")
    assert hasattr(item, "url")
    assert hasattr(item, "description")
    assert item.source.name == 'yandex'

def test_result_priority(results):
    item = results[1]
    assert item.priority == 1