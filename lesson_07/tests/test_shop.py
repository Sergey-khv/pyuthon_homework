from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_shop(driver_firefox):
    login = LoginPage(driver_firefox)
    login.open()
    login.login("standard_user", "secret_sauce")

    main = MainPage(driver_firefox)
    main.add_backpack()
    main.add_bolt_tshirt()
    main.add_onesie()
    main.go_to_cart()

    cart = CartPage(driver_firefox)
    cart.checkout()

    checkout = CheckoutPage(driver_firefox)
    checkout.fill_form("Иван", "Иванов", "123456")
    total = checkout.get_total()

    assert total == "Total: $58.29"
