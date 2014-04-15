from multiprocessing.dummy import Pool as ThreadPool
import time, os
import gevent
from gevent import monkey;
monkey.patch_socket()

from engines.bing import BingEngine
from engines.duckgo import DuckgoEngine
from engines.faroo import FarooEngine
from engines.yandex import YandexEngine


faroo = FarooEngine(configs={
            "api_key": os.environ["FAROO_API_KEY"]
        })

bing = BingEngine(configs={
            "api_key": os.environ["BING_API_KEY"]
        })

duckgo = DuckgoEngine()

yandex = YandexEngine(configs={
            "api_key": os.environ["YANDEX_API_KEY"],
            "username": os.environ["YANDEX_USER_NAME"]
        })

engines = [faroo, duckgo, yandex]

start = time.time()
results = map(lambda x: x.search("python"), engines)
print 'Normail', time.time() - start

start2 = time.time()
pool = ThreadPool(processes=len(engines))
results2 = pool.map(lambda x: x.search("python"), engines)
pool.close()
pool.join()
print 'Thread Pool:', time.time() - start2


start3 = time.time()
jobs = [gevent.spawn(engine.search, "python") for engine in engines]
gevent.joinall(jobs, timeout=4)
print 'Gevent:', time.time() - start3