import pytest
from selenium import webdriver


@pytest.fixture
def driver_chrome():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def driver_firefox():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()
