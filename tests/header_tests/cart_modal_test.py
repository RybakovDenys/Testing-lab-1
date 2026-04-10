def test_cart_modal_opens(homepage):
    cart_modal = homepage.open_cart_modal()
    assert cart_modal.is_displayed()