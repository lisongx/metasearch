from abc import ABCMeta, abstractmethod

import requests


class EngineBase(object):

    _metaclass__ = ABCMeta

    # the weight of search engine, from 0 - 10
    weight = 5

    def __init__(self, **kwargs):
        super(EngineBase, self).__init__()
        for attr, value in kwargs.iteritems():
            setattr(self, attr, value)
        self.config()

    def search(self, query, **kwargs):
        raw_data = self._send_request(query, **kwargs)
        cleaned_data = self._clean_raw_data(raw_data)
        results = self.fill_priority(cleaned_data)
        return results
    
    # configis
    def config(self):
        pass

    # params clean and send the request to the search engine
    def _send_request(self, query, **kwargs):
        pass

    def _clean_raw_data(self, raw_data):
        return raw_data

    def fill_priority(self, data):
        # 0 means biggest
        for i, item in enumerate(data):
            item.priority = i
        return data


class RequestEngine(EngineBase):
    pass
    """base class for engines that we request a url"""


class ResultItemBase(object):
    source = EngineBase

    def __new__(cls, *args, **kwargs):
            obj = object.__new__(cls, *args, **kwargs)
            obj.source = cls.source
            return obj
