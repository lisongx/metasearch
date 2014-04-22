from operator import add, attrgetter
from itertools import groupby

import gevent
import urlnorm
# gevent's monkey patch
from gevent import monkey
monkey.patch_all()

from engines.base import EngineBase


class Aggregator(object):

    def __init__(self):
        self._engines  = []

    def add_engine(self, engine):
        self._check_engine(engine)
        self._engines.append(engine)

    def add_engines(self, engines):
        for engine in engines:
            self._engines.append(engine)

    def _check_engine(self, engine):
        if not isinstance(engine, EngineBase):
            raise Exception("Need to be an engine!")

        for item in self._engines:
            if item.__class__ == engine.__class__:
                raise Exception("Engine already exist!")

    def remove_engine(self, engine_name):
        for item in self._engines:
            if item.name  == engine_name:
                self._engines.remove(item)
                break
    
    def search(self, query, **kwargs):
        raw_results = self._search(query, **kwargs)
        results = self._clean_duplicate(raw_results)
        return results

    def _search(self, query, **kwargs):
        jobs = [gevent.spawn(engine.search, query, **kwargs) for engine in self._engines]
        gevent.joinall(jobs)
        return reduce(add, map(lambda x: x.value, jobs))

    def _clean_duplicate(self, raw_results):
        results = []
        for _, g in groupby(raw_results, attrgetter("url")):
            gs = list(g)
            item = gs[0]
            item.duplicates = len(gs) - 1
            results.append(item)
        return results

    def _sort(self, results):
        keyfunc = lambda x: (1.0 * x.priority) / (x.source.weight + x.duplicates*3)
        return sorted(results, key=keyfunc)
