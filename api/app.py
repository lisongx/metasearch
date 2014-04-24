from engines import ALL_SUPPORT_ENGINES
from aggregator import meta_engine

from flask import request, url_for
from flask.ext.api import FlaskAPI

app = FlaskAPI(__name__)


@app.route('/engines/', methods=['GET'])
def all_engines():
    return [item.as_json() for item in ALL_SUPPORT_ENGINES]


@app.route('/search/', methods=['GET', 'POST'])
def search():
    weights = request.data.get('weights', '')
    q = str(request.data.get('q', ''))

    if weights:
        meta_engine.set_weights(weights)
    
    if q:
        results = meta_engine.search(q)
        return results        
    else:
        return []
