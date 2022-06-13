import typing


class AdFactory:

    # ad: typing.Optional[Ad]

    def __init__(
        self,
        subject="Test subject",
        body="Test body",
        price=1000,
        currency="SEK",
        email="tester@gmail.com",
    ):
        from classified_ads_crud.models.ad import Ad

        ad: Ad = Ad(
            subject=subject, body=body, price=price, currency=currency, email=email
        )
        self.ad = ad

    def get_object(self):
        # use a real factory later ?
        return self.ad
