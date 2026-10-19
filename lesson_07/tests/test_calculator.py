from pages.calculator_page import CalculatorPage


def test_calculator(driver_chrome):
    page = CalculatorPage(driver_chrome)
    page.open()
    page.set_delay("45")

    page.press("7")
    page.press("+")
    page.press("8")
    page.press("=")

    result = page.get_result()
    assert result == "15"
