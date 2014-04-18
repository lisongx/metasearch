from engines.base import ResultItemBase


class Result(ResultItemBase):

    def __init__(self, url, title, description):
        self.url = url
        self.title = title
        self.description = description