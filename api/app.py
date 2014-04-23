from engines import ALL_SUPPORT_ENGINES
from aggregator import meta_engine

from flask import request, url_for
from flask.ext.api import FlaskAPI

app = FlaskAPI(__name__)


@app.route('/engines/')
def all_engines():
    return [item.metadata for item in ALL_SUPPORT_ENGINES]


@app.route('/search/')
def search():
    meta_engine.search(query)
    return [item.metadata for item in ALL_SUPPORT_ENGINES]
