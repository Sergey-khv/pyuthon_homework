from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
import allure


@allure.feature("Интернет-магазин")
@allure.title("Оформление заказа из трёх товаров")
@allure.description("Тест проверяет полный сценарий покупки: авторизация, "
                    "добавление трёх товаров в корзину, оформление заказа "
                    "и проверка итоговой суммы.")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop(driver_firefox):
    """
    Тест проверяет оформление заказа и итоговую сумму.

    :param driver_firefox: WebDriver — объект драйвера Firefox,
                           переданный фикстурой.
    """
    login = LoginPage(driver_firefox)
    main = MainPage(driver_firefox)
    cart = CartPage(driver_firefox)
    checkout = CheckoutPage(driver_firefox)

    with allure.step("Открытие страницы авторизации"):
        login.open()

    with allure.step("Авторизация пользователем standard_user"):
        login.login("standard_user", "secret_sauce")

    with allure.step("Добавление трёх товаров в корзину"):
        main.add_backpack()
        main.add_bolt_tshirt()
        main.add_onesie()

    with allure.step("Переход в корзину"):
        main.go_to_cart()

    with allure.step("Переход к оформлению заказа"):
        cart.checkout()

    with allure.step("Заполнение формы оформления заказа"):
        checkout.fill_form("Иван", "Иванов", "123456")

    with allure.step("Проверка итоговой суммы"):
        with allure.step("Получение итоговой суммы"):
            total = checkout.get_total()
        with allure.step(f"Сравнение итоговой суммы с 'Total: $58.29' "
                         f"(получено: {total})"):
            assert total == "Total: $58.29", (
                f"Ожидаемая сумма: Total: $58.29, но получена: {total}"
            )
