from selenium.webdriver.common.by import By
import allure


class CartPage:
    def __init__(self, driver):
        """
        Конструктор класса CartPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver

    @allure.step("Переход к оформлению заказа")
    def checkout(self):
        """
        Нажимает кнопку 'Checkout' в корзине.

        :return: None
        """
        self.driver.find_element(By.ID, "checkout").click()
