import os

from .bing import BingEngine
from .duckgo import DuckgoEngine
from .faroo import FarooEngine
from .yandex import YandexEngine


bing = BingEngine(api_key=os.environ["BING_API_KEY"])
duckduckgo = DuckgoEngine()
faroo = FarooEngine(api_key=os.environ["FAROO_API_KEY"])
yandex = YandexEngine(
        api_key=os.environ["YANDEX_API_KEY"],
        username=os.environ["YANDEX_USER_NAME"]
    )


ALL_SUPPORT_ENGINES = [
    bing,
    duckduckgo,
    faroo,
    yandex
]