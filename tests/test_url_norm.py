# -*- coding: utf-8 -*-

import pytest
import urlnorm
from tests import Result, TestEngine
from engines.base import ResultItemBase

@pytest.fixture(scope="module")
def test_engine():
    engine = TestEngine(weight=0.5)
    return engine

def make_result(url, title=u"test title", description=u"test desc"):
    item = Result.new(url, title, description, source=test_engine)
    return item

def test_url_end_slash():
    result = make_result(url=u"http://www.baidu.com")
    assert result.url == u"http://www.baidu.com/"