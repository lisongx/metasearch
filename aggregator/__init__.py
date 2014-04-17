import gevent
from gevent import monkey
monkey.patch_socket()

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
    
    def search(self, query, **kwarg):
        jobs = [gevent.spawn(engine.search, query, **kwarg) for engine in self._engines]
        gevent.joinall(jobs)
        results = map(lambda x: x.value, jobs)
        return results