def test_search_functionality(homepage):
    homepage.search("MacBook")
    result_title = homepage.get_page_title_text()
    assert "MacBook" in result_title
