from .base import RequestEngine,  ResultItemBase

import wikipedia


class WikipediaEngine(RequestEngine):
    """
    Wikipedia
    """
    name = "wikipedia"
    url = "http://www.wikipedia.org/"

    DEFAULT_WEIGHT = 1.0

    def _send_request(self, query, **kwargs):
        lang = kwargs.pop("lang", self.DEFAULT_LANG)

        wikipedia.set_lang(lang)
        try:
            page = wikipedia.page(query, auto_suggest=True, redirect=True, preload=True)
            return page
        except (wikipedia.PageError, wikipedia.DisambiguationError) as e:
            return None

    def _clean_raw_data(self, raw_data):
        if raw_data:
            item = WikiPediaResultItem.new(raw_data, source=self)
            return [item]
        else:
            return []


class WikiPediaResultItem(ResultItemBase):

    def __init__(self, data):
        self.url = data.url
        self.title = data.title
        try:
            self.image = data.images[-1]
        except IndexError:
            self.image = None
        self.description = data.summary