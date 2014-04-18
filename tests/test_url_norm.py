# -*- coding: utf-8 -*-

import os
import urlnorm
from engines.base import ResultItemBase

def make_result(url, title=u"test title", description=u"test desc"):
    class Result(ResultItemBase):

        def __init__(self, url, title, description):
            self.url = url
            self.title = title
            self.description = description

    item = Result.new(url, title, description)
    return item

def test_url_end_slash():
    result = make_result(url=u"http://www.baidu.com")
    assert result.url == u"http://www.baidu.com/"