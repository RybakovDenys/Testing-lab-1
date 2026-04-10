def test_brand_filter_applies_correctly(product_page):
    product_page.search("Телевізори")
    product_page.apply_brand_filter("samsung")

    first_product_title = product_page.get_first_product_title()
    assert "SAMSUNG" in first_product_title