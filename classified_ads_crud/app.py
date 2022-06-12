from flask import Flask
from flask_restful import Api

from classified_ads_crud.resources.api_v1.ads_v1.ad_resources_v1 import AdResourceV1
from classified_ads_crud.resources.api_v1.ads_v1.ads_resources_v1 import AdsResourceV1

app = Flask(__name__)
api = Api(app)


api.add_resource(AdsResourceV1, "/api/v1/ads/")
api.add_resource(AdResourceV1, "/api/v1/ads/<int:id>/")

if __name__ == "__main__":
    app.run()
