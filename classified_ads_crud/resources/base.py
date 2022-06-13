import http
import json
from functools import wraps

import flask_restful
from flask import make_response
from flask_restful import Resource


def creation_post_response(f):
    # This is used to send a custom http.HTTPStatus.CREATED response.
    @wraps(f)
    def post_responder(*args, **kwargs):
        response = f(*args, **kwargs)
        return make_response(json.dumps(response), http.HTTPStatus.CREATED)

    return post_responder


class ResourceDoesNotExist(Exception):
    pass


class ResourceBase(Resource):
    def dispatch_request(self, *args, **kwargs):
        try:
            return super().dispatch_request(*args, **kwargs)
        except Exception as ex:
            flask_restful.abort(400, **{"message": str(ex)})
