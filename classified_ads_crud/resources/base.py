import http

import flask_restful
from flask import Response
from flask_restful import Resource


class ResourceDoesNotExist(Exception):
    pass


class ResourceBase(Resource):
    def dispatch_request(self, *args, **kwargs):
        try:
            super().dispatch_request(*args, **kwargs)
        except Exception as ex:
            flask_restful.abort(400, **{"message": str(ex)})
