import typing
from dataclasses import dataclass

from sqlalchemy import asc, desc

from classified_ads_crud.database import db_session
from classified_ads_crud.models.ad import Ad
from classified_ads_crud.schemas.schemas_v1.ad_schema_v1 import AdSchemaV1


@dataclass
class SortArgsDTO:
    sort: str = "created_at"  # default.
    order_by: str = "desc"  # default


class AdsServicesV1(object):
    def get_all_ads(self, sort_args: SortArgsDTO):
        if sort_args.order_by == "desc":
            applied_sort = desc(sort_args.sort)
        else:
            applied_sort = asc(sort_args.sort)

        return Ad.query.order_by(applied_sort).all()

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
