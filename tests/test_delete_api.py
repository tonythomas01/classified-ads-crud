import http
import json

from tests.factories import AdFactory


def test_delete_api_existing(client):
    from classified_ads_crud.database import db_session
    from classified_ads_crud.models.ad import Ad

    ad_object = AdFactory().get_object()
    with db_session() as session:
        session.add(ad_object)
        session.commit()
        session.flush()
        session.refresh(ad_object)

    assert Ad.query.count() == 1

    # NOw, lets try to delete it
    delete_response = client.delete(f"/api/v1/ads/{ad_object.id}/")
    # now check the number of ads
    assert Ad.query.count() == 0


def test_delete_api_non_existing(client):

    # NOw, lets try to delete it
    delete_response = client.delete(f"/api/v1/ads/2442/")
    # now check the number of ads
    assert delete_response.status_code == 400
