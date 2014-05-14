# -*- coding: utf-8 -*-

from engines import ALL_SUPPORT_ENGINES
from aggregator import meta_engine

from flask import request, url_for
from flask.ext.api import FlaskAPI, status, exceptions

from .utils import get_lang

app = FlaskAPI(__name__)


@app.route('/engines/', methods=['GET'])
def all_engines():
    return [item.as_json() for item in ALL_SUPPORT_ENGINES]


@app.route('/search/', methods=['GET'])
def search():
    q = request.args.get('q', '')

    if not q:
        return []

    try:
        weights = {
            key.split('-')[1]: float(value)
            for key, value in request.args.iteritems()
            if key.startswith("weight-")
        }
    except Exception as e:
        raise e

    kwargs  = {}

    #  get the query text's language first from querystring, then guess
    lang = request.args.get('lang', '')
    if not lang:
        lang = get_lang(q)
    kwargs["lang"] = lang

    engines = request.args.get("engines", '')

    if engines:
        engines = engines.split(',')
        kwargs["engines"] = engines

    page = int(request.data.get('page', 0))

    if page > 0:
        kwargs["page"] = page

    if weights:
        meta_engine.set_weights(weights)

    results = meta_engine.search(q, **kwargs)
    results =  [item.as_json() for item in results]
    return results