from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

        self.cart_icon_clickable = EC.element_to_be_clickable((By.CLASS_NAME, "header-basket"))
        self.cart_modal_visible = EC.visibility_of_element_located((By.ID, "empty-cart-popup"))
        self.city_button_clickable = EC.element_to_be_clickable((By.CLASS_NAME, "header__sub-region"))
        self.city_input_visible = EC.visibility_of_element_located((By.ID, "city-search"))
        self.city_popup_invisible = EC.invisibility_of_element_located((By.CLASS_NAME, "popup__cities"))
        self.login_icon_clickable = EC.element_to_be_clickable((By.CLASS_NAME, "header__sub-user"))
        self.login_modal_visible = EC.visibility_of_element_located((By.CLASS_NAME, "auth"))
        self.search_input_visible = EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='search']"))
        self.search_button_clickable = EC.element_to_be_clickable((By.CSS_SELECTOR, ".header-search__button"))
        self.page_title_present = EC.presence_of_element_located((By.TAG_NAME, "h1"))

    def city_result_clickable(self, city_name):
        return EC.element_to_be_clickable(
            (
                By.XPATH,
                f"//ul[contains(@class, 'popup__cities')]//span[contains(text(), '{city_name}')]",
            )
        )

    def city_button_contains(self, city_name):
        return EC.text_to_be_present_in_element((By.CLASS_NAME, "header__sub-region"), city_name)

    def brand_checkbox_clickable(self, brand_token):
        return EC.element_to_be_clickable(
            (
                By.XPATH,
                f"//input[@data-token='{brand_token}']/parent::label",
            )
        )

    def url_contains_brand(self, brand_token):
        return EC.url_contains(brand_token)

    def open_cart_modal(self):
        cart_icon_element = self.wait.until(self.cart_icon_clickable)
        cart_icon_element.click()
        cart_modal_element = self.wait.until(self.cart_modal_visible)
        return cart_modal_element

    def open_login_modal(self):
        login_icon_element = self.wait.until(self.login_icon_clickable)
        login_icon_element.click()
        login_modal_element = self.wait.until(self.login_modal_visible)
        return login_modal_element

    def change_city(self, city_name):
        city_button_element = self.wait.until(self.city_button_clickable)
        city_button_element.click()

        city_input_element = self.wait.until(self.city_input_visible)
        city_input_element.clear()
        city_input_element.send_keys(city_name)

        city_result_element = self.wait.until(self.city_result_clickable(city_name))
        city_result_element.click()

        self.wait.until(self.city_popup_invisible)
        return self.wait.until(self.city_button_contains(city_name))

    def search(self, query):
        search_input_element = self.wait.until(self.search_input_visible)
        search_input_element.clear()
        search_input_element.send_keys(query)

        search_button_element = self.wait.until(self.search_button_clickable)
        search_button_element.click()

    def apply_brand_filter(self, brand_token):
        brand_checkbox_element = self.wait.until(self.brand_checkbox_clickable(brand_token))
        brand_checkbox_element.click()
        return self.wait.until(self.url_contains_brand(brand_token))

    def get_page_title_text(self):
        page_title_element = self.wait.until(self.page_title_present)
        return page_title_element.text
