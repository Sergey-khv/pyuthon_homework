from pages.calculator_page import CalculatorPage
import allure


@allure.feature("Калькулятор")
@allure.title("Проверка сложения 7 + 8 = 15 с задержкой 45 секунд")
@allure.description("Тест проверяет, что калькулятор корректно выполняет "
                    "сложение 7 и 8 при задержке вывода результата 45 секунд.")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator(driver_chrome):
    """
    Тест проверяет работу калькулятора: 7 + 8 = 15.

    :param driver_chrome: WebDriver — объект драйвера Chrome,
                          переданный фикстурой.
    """
    page = CalculatorPage(driver_chrome)

    with allure.step("Открытие страницы калькулятора"):
        page.open()

    with allure.step("Установка задержки 45 секунд"):
        page.set_delay("45")

    with allure.step("Нажатие кнопок: 7, +, 8, ="):
        page.press("7")
        page.press("+")
        page.press("8")
        page.press("=")

    with allure.step("Проверка результата"):
        with allure.step("Ожидание и получение результата с экрана"):
            result = page.get_result()
        with allure.step(f"Сравнение результата с ожидаемым '15' "
                         f"(получено: {result})"):
            assert result == "15", (
                f"Ожидаемый результат: 15, но получен: {result}"
            )
