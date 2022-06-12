import typing

from classified_ads_crud.database import db_session
from classified_ads_crud.models.ad import Ad
from classified_ads_crud.schemas.schemas_v1.ad_schema_v1 import AdSchemaV1


class AdsServicesV1(object):
    def get_all_ads(self):
        return Ad.query.all()

    def serialize_ads(self, ads: typing.List[Ad]):
        ad_schema = AdSchemaV1()
        return ad_schema.dump(ads, many=True)

    def serialize_ad(self, ad: Ad):
        ad_schema = AdSchemaV1()
        return ad_schema.dump(ad, many=False)

    def create_ad(self, incoming_ad: typing.Dict[str, typing.Any]) -> Ad:
        ad: Ad = Ad(**incoming_ad)
        with db_session() as session:
            session.add(ad)
            session.commit()
            session.flush()
            session.refresh(ad)
            return ad
