from flask import Flask
from flask_marshmallow import Marshmallow
from flask_restful import Api


from config import Config


def create_app():
    app = Flask(__name__)
    api = Api(app)
    app.config.from_object(Config)

    with app.app_context():
        from classified_ads_crud.database import init_db, db_session

        init_db()

    ma = Marshmallow(app)

    from classified_ads_crud.resources.api_v1.ad_resources_v1 import AdResourceV1
    from classified_ads_crud.resources.api_v1.ads_resources_v1 import AdsResourceV1

    api.add_resource(AdsResourceV1, "/api/v1/ads/")
    api.add_resource(AdResourceV1, "/api/v1/ads/<int:ad_id>/")

    # Requirement, for decalarative for thread safety.
    # See https://flask.palletsprojects.com/en/2.1.x/patterns/sqlalchemy/
    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()

    return app
