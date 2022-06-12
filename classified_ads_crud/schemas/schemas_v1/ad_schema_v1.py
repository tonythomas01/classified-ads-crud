from marshmallow import fields

from classified_ads_crud.app import ma


class AdSchemaV1(ma.SQLAlchemyAutoSchema):
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
