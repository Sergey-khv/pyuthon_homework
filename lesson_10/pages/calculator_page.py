from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CalculatorPage:
    def __init__(self, driver):
        """
        Конструктор класса CalculatorPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver

    @allure.step("Открытие страницы калькулятора")
    def open(self):
        """
        Открывает страницу калькулятора.

        :return: None
        """
        url = (
            "https://bonigarcia.dev/"
            "selenium-webdriver-java/slow-calculator.html"
        )
        self.driver.get(url)

    @allure.step("Установка задержки {value} секунд")
    def set_delay(self, value):
        """
        Устанавливает задержку для выполнения операций на калькуляторе.

        :param value: int — время задержки в секундах.
        :return: None
        """
        field = self.driver.find_element(By.ID, "delay")
        field.clear()
        field.send_keys(value)

    @allure.step("Нажатие кнопки '{button}'")
    def press(self, button):
        """
        Нажимает на кнопку калькулятора.

        :param button: str — текст на кнопке, которую нужно нажать.
        :return: None
        """
        xpath = f"//span[text()='{button}']"
        self.driver.find_element(By.XPATH, xpath).click()

    @allure.step("Ожидание результата и получение его с экрана")
    def get_result(self, timeout=50):
        """
        Ожидает появления результата '15' на экране и возвращает его.

        :param timeout: int — максимальное время ожидания в секундах.
        :return: str — текст результата на экране калькулятора.
        """
        wait = WebDriverWait(self.driver, timeout)
        wait.until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
        )
        return self.driver.find_element(By.CLASS_NAME, "screen").text
