from abc import ABCMeta, abstractmethod

import requests


class EngineBase(object):
    _metaclass__ = ABCMeta

    def __init__(self, configs={}):
        super(EngineBase, self).__init__()
        for attr, value in configs.iteritems():
            setattr(self, attr, value)
        self.config()

    def search(self, query, **kwargs):
        raw_data = self.send_request(query, **kwargs)
        return self.clean_raw_data(raw_data)
    
    # configis
    def config(self):
        pass

    # params clean
    def send_request(self, query, **kwargs):
        pass

    def clean_raw_data(self, raw_data):
        return raw_data


class RequestEngine(EngineBase):
    pass
    """base class for engines that we request a url"""