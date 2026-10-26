from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = (
            "https://bonigarcia.dev/"
            "selenium-webdriver-java/slow-calculator.html"
        )
        self.driver.get(url)

    def set_delay(self, value):
        field = self.driver.find_element(By.ID, "delay")
        field.clear()
        field.send_keys(value)

    def press(self, button):
        xpath = f"//span[text()='{button}']"
        self.driver.find_element(By.XPATH, xpath).click()

    def get_result(self, timeout=50):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
        )
        return self.driver.find_element(By.CLASS_NAME, "screen").text
