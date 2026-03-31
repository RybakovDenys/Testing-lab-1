import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestFoxtrot:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 5)
        self.driver.get("https://www.foxtrot.com.ua/")

    def teardown_method(self):
        self.driver.quit()

    def test_search_functionality(self):
        search_input = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='search']"))
        )
        search_input.send_keys("MacBook")
        
        search_button = self.driver.find_element(By.CSS_SELECTOR, ".header-search__button")
        search_button.click()
        
        result_title = self.wait.until(
            EC.presence_of_element_located((By.TAG_NAME, "h1"))
        )
        assert "MacBook" in result_title.text


    def test_cart_modal_opens(self):
        cart_icon = self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "header-basket"))
        )
        cart_icon.click()
        
        cart_modal = self.wait.until(
            EC.visibility_of_element_located((By.ID, "empty-cart-popup"))
        )
        assert cart_modal.is_displayed()

    def test_login_modal_opens(self):
        login_icon = self.wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "header__sub-user"))
        )
        login_icon.click()
        
        login_modal = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "auth"))
        )
        assert login_modal.is_displayed()

    def test_brand_filter_applies_correctly(self):
        search_input = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='search']"))
        )
        search_input.send_keys("Телевізори")
        self.driver.find_element(By.CSS_SELECTOR, ".header-search__button").click()

        samsung_checkbox = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@data-token='samsung']/parent::label"))
        )

        samsung_checkbox.click()
        
        self.wait.until(EC.url_contains("samsung")) 

        first_product_title = self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "product-card__title"))
        )
        assert "SAMSUNG" in first_product_title.text

    def test_change_city_in_header(self):
        header_city_btn = self.wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "header__sub-region"))
        )
        header_city_btn.click()

        city_input = self.wait.until(
            EC.visibility_of_element_located((By.ID, "city-search"))
        )
        city_input.send_keys("Львівське")

        city_result = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//ul[contains(@class, 'popup__cities')]//span[contains(text(), 'Львівське')]"))
        )
        city_result.click()

        self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "popup__cities")))

        city_updated = self.wait.until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "header__sub-region"), "Львівське")
        )
        assert city_updated is True