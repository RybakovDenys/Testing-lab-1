import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from pages.homepage import HomePage
from pages.product_page import ProductPage

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.foxtrot.com.ua/")
    
    yield driver 

    driver.quit()

@pytest.fixture(scope="function")
def wait(driver):
    return WebDriverWait(driver, 5)

@pytest.fixture(scope="function")
def homepage(driver, wait):
    return HomePage(driver, wait)

@pytest.fixture(scope="function")
def product_page(driver, wait):
    return ProductPage(driver, wait)