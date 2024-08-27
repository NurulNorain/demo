import pytest
from selenium import webdriver
import time


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()


