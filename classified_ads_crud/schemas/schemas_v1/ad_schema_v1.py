from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


class AdSchemaV1(SQLAlchemyAutoSchema):
    created_at = fields.DateTime(
        data_key="createdAt",
        attribute="created_at",
        dump_only=True,
    )  # For snakeCase.

    class Meta:
        from classified_ads_crud.models.ad import Ad

        model = Ad
        exclude = (
            "updated_at",
            "deleted",
        )
