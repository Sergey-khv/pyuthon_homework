from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import (
    expected_conditions as EC,
)


def test_01_form():
    driver = webdriver.Edge()
    wait = WebDriverWait(driver, 10)

    # Открываем страницу
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/"
        "data-types.html"
    )

    # Заполняем форму
    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    # zip-code оставляем пустым
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    # Нажимаем Submit
    driver.find_element(
        By.CSS_SELECTOR, "button[type='submit']"
    ).click()

    # Ждём, пока появятся классы валидации
    wait.until(
        EC.presence_of_element_located(
            (By.CLASS_NAME, "alert-danger")
        )
    )

    # Проверяем, что Zip code красный
    zip_code = driver.find_element(By.ID, "zip-code")
    assert "alert-danger" in zip_code.get_attribute("class")

    # Проверяем, что остальные поля зелёные
    first_name = driver.find_element(By.ID, "first-name")
    assert "alert-success" in first_name.get_attribute("class")

    last_name = driver.find_element(By.ID, "last-name")
    assert "alert-success" in last_name.get_attribute("class")

    address = driver.find_element(By.ID, "address")
    assert "alert-success" in address.get_attribute("class")

    email = driver.find_element(By.ID, "e-mail")
    assert "alert-success" in email.get_attribute("class")

    phone = driver.find_element(By.ID, "phone")
    assert "alert-success" in phone.get_attribute("class")

    city = driver.find_element(By.ID, "city")
    assert "alert-success" in city.get_attribute("class")

    country = driver.find_element(By.ID, "country")
    assert "alert-success" in country.get_attribute("class")

    job = driver.find_element(By.ID, "job-position")
    assert "alert-success" in job.get_attribute("class")

    company = driver.find_element(By.ID, "company")
    assert "alert-success" in company.get_attribute("class")

    driver.quit()
