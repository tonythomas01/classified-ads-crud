from classified_ads_crud.resources.base import ResourceBase
from classified_ads_crud.services.services_v1.ad_service_v1 import AdServiceV1


class AdResourceV1(ResourceBase):
    def get(self, ad_id):
        ad_service_v1: AdServiceV1 = AdServiceV1.new_from_id(id=ad_id)
        return ad_service_v1.serialize_ad()

    def delete(self, ad_id):
        ad_service_v1: AdServiceV1 = AdServiceV1.new_from_id(id=ad_id)
        ad_service_v1.delete_ad()
        return None
