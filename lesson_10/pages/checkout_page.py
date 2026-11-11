from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CheckoutPage:
    def __init__(self, driver):
        """
        Конструктор класса CheckoutPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver

    @allure.step("Заполнение формы оформления заказа")
    def fill_form(self, first_name, last_name, zip_code):
        """
        Заполняет форму оформления заказа и нажимает 'Continue'.

        :param first_name: str — имя.
        :param last_name: str — фамилия.
        :param zip_code: str — почтовый индекс.
        :return: None
        """
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(zip_code)
        self.driver.find_element(By.ID, "continue").click()

    @allure.step("Получение итоговой суммы заказа")
    def get_total(self):
        """
        Ожидает появления итоговой суммы и возвращает её.

        :return: str — текст итоговой суммы.
        """
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "summary_total_label")
            )
        )
        return element.text
