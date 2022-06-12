import marshmallow
from marshmallow import fields, validate, post_load
from marshmallow.schema import BaseSchema


class RequestArgsV1(BaseSchema):
    sort = fields.Str(
        required=False,
        validate=validate.OneOf(["creation", "price"]),
        default="creation",
    )
    order_by = fields.Str(
        data_key="orderBy",
        required=False,
        default="desc",
        validate=validate.OneOf(["asc", "desc"]),
        missing=marshmallow.missing,
    )

    @post_load
    def transform_sort(self, in_data, **kwargs):
        if in_data["sort"] == "creation":
            in_data["sort"] = "created_at"
        return in_data
