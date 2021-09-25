from selenium import webdriver
import pytest


@pytest.fixture
def browser():
    driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
    driver.implicitly_wait(5)
    yield driver
    driver.quit()
