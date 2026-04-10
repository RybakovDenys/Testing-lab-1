def test_change_city_in_header(homepage):
    city_updated = homepage.change_city("Львівське")
    assert city_updated is True