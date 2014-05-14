from abc import ABCMeta, abstractmethod
import requests
import urlnorm


class EngineBase(object):

    _metaclass__ = ABCMeta

    # the weight of search engine, from 0 - 1.0
    DEFAULT_LANG = "en"
    DEFAULT_WEIGHT = 0.5
    RESULT_MAX_LIMIT = 10

    def __init__(self, **kwargs):
        super(EngineBase, self).__init__()
        self.config(**kwargs)

    def search(self, query, **kwargs):
        # transform page to start
        if "page" in kwargs:
            kwargs["start"] =  (kwargs["page"] - 1) * self.RESULT_MAX_LIMIT

        raw_data = self._send_request(query, **kwargs)
        cleaned_data = self._clean_raw_data(raw_data)
        results = self.fill_priority(cleaned_data)
        return results

    def config(self, **kwargs):
        for attr, value in kwargs.iteritems():
            setattr(self, attr, value)
        if "weight" not in kwargs:
            self.weight = self.DEFAULT_WEIGHT

        self._post_config()

    # init api library or client
    def _post_config(self):
        pass

    # params clean and send the request to the search engine
    # --- kwargs ---
    # start: the start item
    # limit: the results limit
    def _send_request(self, query, **kwargs):
        pass

    def _clean_raw_data(self, raw_data):
        return raw_data

    def fill_priority(self, data):
        # result order in their source engine
        for i, item in enumerate(data):
            item.priority = i + 1
        return data

    def as_json(self):
        return {
            "name": self.name,
            "url": self.url,
            "weight": self.weight
        }



class RequestEngine(EngineBase):
    pass
    """base class for engines that we request a url"""


class ResultItemBase(object):

    @classmethod
    def new(cls, *args, **kwargs):
        obj = cls(*args)
        obj.source = kwargs['source']
        obj.duplicates = 0
        obj.priority = 0
        # normalize url
        if hasattr(obj, 'url'):
            obj.url = urlnorm.norm(obj.url)
        return obj

    def __unicode__(self):
        return u"%s/priority-%s/duplicates-%s" % (self.__class__, self.priority, self.duplicates)

    def as_json(self):
        return {
            "title": self.title,
            "url": self.url,
            "description": self.description,
            "image": self.image,
            "source": self.source.as_json()
        }