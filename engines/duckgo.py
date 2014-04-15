import duckduckgo

from .base import EngineBase


class DuckgoEngine(EngineBase):

    TYPES = {
        'ANSWER': u'answer',
        'DISAMBIGUATION': u'disambiguation'
    }

    def _send_request(self, query, **kwargs):
        return duckduckgo.query(query)

    def _clean_raw_data(self, raw_data):
        if raw_data.type == self.TYPES['ANSWER']:
            return raw_data.results
        elif raw_data.type == self.TYPES['DISAMBIGUATION']:
            return raw_data.related
        else:
            return []