from classified_ads_crud.database import db_session

from classified_ads_crud.models.ad import Ad
from classified_ads_crud.resources.base import ResourceDoesNotExist
from classified_ads_crud.services.services_v1.ads_services_v1 import AdsServicesV1


class AdServiceV1(AdsServicesV1):
    ad: Ad = None

    def __init__(self, ad: Ad):
        self.ad = ad

    def serialize_ad(self):
        # Hack, but probably for the better.
        return super().serialize_ad(self.ad)

    @classmethod
    def new_from_id(cls, id: int):
        with db_session() as session:
            ad: Ad = session.query(Ad).get(int(id))
            if not ad:
                raise ResourceDoesNotExist(
                    f"An ad with id: {id} does not " f"exist."
                )  #
                # Catched outside.
            return cls(ad=ad)

    def delete_ad(self):
        # @TODO: Replace wiht a soft delete.
        with db_session() as session:
            session.delete(self.ad)
            session.commit()
