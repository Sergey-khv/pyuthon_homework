import pytest
from selenium import webdriver


@pytest.fixture
def driver_chrome():
    """
    Фикстура для инициализации и завершения работы драйвера Chrome.
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def driver_firefox():
    """
    Фикстура для инициализации и завершения работы драйвера Firefox.
    """
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()
