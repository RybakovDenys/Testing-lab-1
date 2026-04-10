from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class ProductPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

        self.search_input_visible = EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='search']"))
        self.search_button_clickable = EC.element_to_be_clickable((By.CSS_SELECTOR, ".header-search__button"))
        self.first_product_title_present = EC.presence_of_element_located((By.CLASS_NAME, "product-card__title"))

    def brand_checkbox_clickable(self, brand_token):
        return EC.element_to_be_clickable(
            (
                By.XPATH,
                f"//input[@data-token='{brand_token}']/parent::label",
            )
        )

    def url_contains_brand(self, brand_token):
        return EC.url_contains(brand_token)

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

    def get_first_product_title(self):
        first_product_title_element = self.wait.until(self.first_product_title_present)
        return first_product_title_element.text