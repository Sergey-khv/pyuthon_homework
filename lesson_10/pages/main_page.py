from selenium.webdriver.common.by import By
import allure


class MainPage:
    def __init__(self, driver):
        """
        Конструктор класса MainPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver

    @allure.step("Добавление рюкзака в корзину")
    def add_backpack(self):
        """
        Добавляет рюкзак Sauce Labs в корзину.

        :return: None
        """
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-backpack"
        ).click()

    @allure.step("Добавление футболки в корзину")
    def add_bolt_tshirt(self):
        """
        Добавляет футболку Sauce Labs Bolt T-Shirt в корзину.

        :return: None
        """
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"
        ).click()

    @allure.step("Добавление комбинезона в корзину")
    def add_onesie(self):
        """
        Добавляет комбинезон Sauce Labs Onesie в корзину.

        :return: None
        """
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-onesie"
        ).click()

    @allure.step("Переход в корзину")
    def go_to_cart(self):
        """
        Переходит на страницу корзины.

        :return: None
        """
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
