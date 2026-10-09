from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_session_storage_auth():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    # Пользователь 1
    driver.get("https://gitflic.ru/")
    driver.maximize_window()

    driver.add_cookie({
        "name": "SESSION",
        "value": "NWQ1YjZmNzMtZjA1Mi00YzgyLWJlODgtZjhjMTEwMGUxM2U4",
        "domain": "gitflic.ru",
    })
    driver.add_cookie({
        "name": "cookiesAccepted",
        "value": "true",
        "domain": "gitflic.ru",
    })

    driver.refresh()
    
    # Ждём, пока страница загрузится после refresh
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    driver.get("https://gitflic.ru/user/paray")
    wait.until(EC.url_contains("/user/"))
    url_user_1 = driver.current_url

    # Разлогиниваемся
    driver.delete_all_cookies()
    
    driver.get("https://gitflic.ru/")
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    # Пользователь 2
    driver.add_cookie({
        "name": "SESSION",
        "value": "NTE1NzNjMWYtM2Y0NC00ZGYxLTg1MmQtNTRhMzA3OWJjODkx",
        "domain": "gitflic.ru",
    })
    driver.add_cookie({
        "name": "cookiesAccepted",
        "value": "true",
        "domain": "gitflic.ru",
    })

    driver.refresh()
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    driver.get("https://gitflic.ru/user/tranzit_27")
    wait.until(EC.url_contains("/user/"))
    url_user_2 = driver.current_url

    assert url_user_1 != url_user_2, (
        f"URL должны отличаться: user_1='{url_user_1}', user_2='{url_user_2}'"
    )

    driver.quit()
