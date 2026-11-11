from selenium.webdriver.common.by import By
import allure


class LoginPage:
    def __init__(self, driver):
        """
        Конструктор класса LoginPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver

    @allure.step("Открытие страницы авторизации")
    def open(self):
        """
        Открывает страницу авторизации saucedemo.

        :return: None
        """
        self.driver.get("https://www.saucedemo.com/")

    @allure.step("Авторизация пользователем {username}")
    def login(self, username, password):
        """
        Выполняет вход с указанными учётными данными.

        :param username: str — имя пользователя.
        :param password: str — пароль.
        :return: None
        """
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()
