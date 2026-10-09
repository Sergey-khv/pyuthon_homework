from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_02_calc():
    driver = webdriver.Chrome()

    # Открываем страницу
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )

    # Вводим задержку 45 секунд
    delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()
    delay_input.send_keys("45")

    # Нажимаем кнопки 7 + 8 =
    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()

    # Ждём, пока в окне появится результат 15
    # Таймаут больше 45, чтобы успеть дождаться
    wait = WebDriverWait(driver, 50)
    wait.until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
    )

    # Проверяем результат
    result = driver.find_element(By.CSS_SELECTOR, ".screen").text
    assert result == "15"

    driver.quit()
