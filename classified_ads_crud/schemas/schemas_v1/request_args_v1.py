import marshmallow
from marshmallow import fields, validate, post_load
from marshmallow.schema import BaseSchema


class RequestArgsV1(BaseSchema):
    sort = fields.Str(
        required=False,
        validate=validate.OneOf(["creation", "price"]),
        default="creation",
        allow_none=True,
    )
    order_by = fields.Str(
        data_key="orderBy",
        required=False,
        default="desc",
        validate=validate.OneOf(["asc", "desc"]),
        missing=marshmallow.missing,
        allow_none=True,
    )

    @post_load
    def transform_sort(self, in_data, **kwargs):
        in_data_sort_param = in_data.get("sort", None)
        if in_data_sort_param and in_data_sort_param == "creation":
            in_data["sort"] = "created_at"
        return in_data
