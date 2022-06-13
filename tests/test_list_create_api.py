import json


def test_create_request_example(client):

    ad_data = {
        "subject": "Ad Name",
        "body": "This is a very short body.",
        "price": 50000,
        "currency": "SEK",
        "email": "teggggter@gmail.com",
    }

    post_response = client.post("/api/v1/ads/", json=ad_data)
    assert post_response.status_code == 201
    from classified_ads_crud.models.ad import Ad

    post_response_parsed = json.loads(post_response.data)
    ad_object: Ad = Ad.query.get(post_response_parsed.get("id"))

    assert ad_object.price == 50000
    assert ad_object.subject == "Ad Name"
