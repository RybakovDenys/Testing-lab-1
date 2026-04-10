def test_login_modal_opens(homepage):
    login_modal = homepage.open_login_modal()
    assert login_modal.is_displayed()