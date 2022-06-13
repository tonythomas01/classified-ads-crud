import typing

import marshmallow
from flask import request

from classified_ads_crud.resources.base import ResourceBase, creation_post_response
from classified_ads_crud.schemas.schemas_v1.ad_schema_v1 import AdSchemaV1
from classified_ads_crud.schemas.schemas_v1.request_args_v1 import RequestArgsV1
from classified_ads_crud.services.services_v1.ads_services_v1 import (
    AdsServicesV1,
    SortArgsDTO,
)


class AdsResourceV1(ResourceBase):
    method_decorators = {"post": [creation_post_response]}
    """
    List and Create handler for ads.
    """

    def post(self):
        request_body = request.get_json()

        incoming_body: typing.Dict[str, typing.Any] = AdSchemaV1().load(
            request_body
        )  # Later, replace with dataclasses.

        ads_service_v1 = AdsServicesV1()
        created_ad = ads_service_v1.create_ad(incoming_ad=incoming_body)
        return ads_service_v1.serialize_ad(ad=created_ad)

    def get(self):
        sort_args: SortArgsDTO = SortArgsDTO()
        try:
            query_args = RequestArgsV1().load(request.args)
            sort_args: SortArgsDTO = SortArgsDTO(**query_args)
        except marshmallow.exceptions.ValidationError:
            # this was a bad argument, just ignore it completely.
            ...

        ads_service_v1 = AdsServicesV1()
        all_ads = ads_service_v1.get_all_ads(sort_args)
        return ads_service_v1.serialize_ads(ads=all_ads)
