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
        self._engines  = {}

    def add_engine(self, engine):
        self._check_engine(engine)
        self._engines[engine.name] = engine

    def add_engines(self, engines):
        for engine in engines:
            self.add_engine(engine)

    def __getitem__(self, key):
        return self._engines[key]

    def _check_engine(self, engine):
        if not isinstance(engine, EngineBase):
            raise Exception("Need to be an engine!")

        if engine.name in self._engines.keys():
            raise Exception("Engine already exist!")

    def remove_engine(self, engine_name):
        self._engines.pop(engine_name)

    def search(self, query, **kwargs):
        raw_results = self._search(query, **kwargs)
        uniq_results = self._clean_duplicate(raw_results)
        results = self._sort(uniq_results)
        return results

    def _search(self, query, **kwargs):
        jobs = [gevent.spawn(engine.search, query, **kwargs) 
                for engine in self._engines.values()]
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
