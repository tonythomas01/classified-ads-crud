from flask_restful import Resource


class AdsResourceV1(Resource):
    def get(self):
        return {"hello": "world"}
