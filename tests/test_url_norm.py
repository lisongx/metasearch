# -*- coding: utf-8 -*-

import urlnorm
from tests import Result
from engines.base import ResultItemBase

def make_result(url, title=u"test title", description=u"test desc"):
    item = Result.new(url, title, description)
    return item

def test_url_end_slash():
    result = make_result(url=u"http://www.baidu.com")
    assert result.url == u"http://www.baidu.com/"