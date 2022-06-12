from flask_restful import Resource


class ResourceDoesNotExist(Exception):
    pass


class ResourceBase(Resource):
    ...
