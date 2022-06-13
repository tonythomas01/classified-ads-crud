import json

from tests.factories import AdFactory


def test_list_of_multiple_ads(client):
    from classified_ads_crud.database import db_session

    # We just create some random objects and try to list it.
    ad_objects = []
    for i in range(5):
        ad_object = AdFactory(price=i).get_object()
        ad_objects.append(ad_object)

    with db_session() as session:
        session.bulk_save_objects(ad_objects)
        session.commit()

    # Just to see if we have the right amount of things here
    from classified_ads_crud.models.ad import Ad

    assert Ad.query.count() == 5

    # Now, try to list it
    get_response = client.get("/api/v1/ads/")
    assert get_response.status_code == 200
    get_response_parsed = json.loads(get_response.data)
    assert len(get_response_parsed["ads"]) == 5

    # Also, try to sort it here ?

    get_response = client.get("/api/v1/ads/?sort=price&orderBy=desc")
    assert get_response.status_code == 200
    get_response_parsed = json.loads(get_response.data)
    assert len(get_response_parsed["ads"]) == 5

    # just check if the last one was returned first.
    assert get_response_parsed["ads"][0]["price"] == 4  # 0 to 4 above in
    # range()
    get_response = client.get("/api/v1/ads/?sort=price&orderBy=asc")
    assert get_response.status_code == 200
    get_response_parsed = json.loads(get_response.data)
    assert len(get_response_parsed["ads"]) == 5

    # just check if the last one was returned first.
    assert get_response_parsed["ads"][0]["price"] == 0  # 0 to 4 above in
    # range()
