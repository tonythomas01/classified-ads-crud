from marshmallow import fields

from classified_ads_crud.app import ma


class AdSchemaV1(ma.SQLAlchemySchema):
    currency = ma.auto_field()
    subject = ma.auto_field()
    body = ma.auto_field()
    price = ma.auto_field()
    email = ma.auto_field()

    createdAt = fields.DateTime(
        attribute="created_at",
        dump_only=True,
    )

    class Meta:
        from classified_ads_crud.models.ad import Ad

        model = Ad
