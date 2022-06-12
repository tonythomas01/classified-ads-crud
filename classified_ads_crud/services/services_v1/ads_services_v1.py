import typing

from classified_ads_crud.database import db_session
from classified_ads_crud.models.ad import Ad
from classified_ads_crud.schemas.schemas_v1.ad_schema_v1 import AdSchemaV1


class AdsServicesV1(object):
    def get_all_ads(self):
        return Ad.query.all()

    def serialize_ads(self, ads: typing.List[typing.Any]):
        ad_schema = AdSchemaV1()
        return ad_schema.dump(ads, many=True)

    def create_ad(self, incoming_ad: typing.Dict[str, typing.Any]) -> Ad:
        ad: Ad = Ad(**incoming_ad)

        db_session.add(ad)
        db_session.commit()
        db_session.flush()
        db_session.refresh(ad)

        return ad
