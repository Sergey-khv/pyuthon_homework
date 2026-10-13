from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_03_shop():
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 10)

    # 1. Открываем сайт магазина
    driver.get("https://www.saucedemo.com/")

    # 2. Авторизуемся
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # 3. Добавляем товары в корзину
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    # 4. Переходим в корзину
    driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()

    # 5. Нажимаем Checkout
    wait.until(
        EC.element_to_be_clickable((By.ID, "checkout"))
    ).click()

    # 6. Заполняем форму своими данными
    wait.until(
        EC.presence_of_element_located((By.ID, "first-name"))
    ).send_keys("Иван")
    driver.find_element(By.ID, "last-name").send_keys("Петров")
    driver.find_element(By.ID, "postal-code").send_keys("123456")

    # 7. Нажимаем Continue
    driver.find_element(By.ID, "continue").click()

    # 8. Читаем итоговую стоимость
    total_element = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".summary_total_label")
            )
    )
    total_text = total_element.text

    # 9. Закрываем браузер
    driver.quit()

    # 10. Проверяем, что итоговая сумма равна $58.29
    assert total_text == "Total: $58.29", (
        f"Ожидалось 'Total: $58.29', получено '{total_text}'"
    )
