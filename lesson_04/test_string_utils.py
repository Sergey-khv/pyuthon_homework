import pytest
from string_utils import StringUtils


string_utils = StringUtils()


# ============================================================
#  capitalize
# ============================================================

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
    ("тест", "Тест"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
    ("04 апреля 2023", "04 апреля 2023"),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


# ============================================================
#  trim
# ============================================================

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    ("skypro", "skypro"),
    ("  hello world", "hello world"),
    ("04 апреля 2023", "04 апреля 2023"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    ("     ", ""),
    ("   ", ""),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


# ============================================================
#  contains
# ============================================================

@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True),
    ("SkyPro", "k", True),
    ("SkyPro", "Pro", True),
    ("123", "2", True),
    (" ", " ", True),
])
def test_contains_positive(string, symbol, expected):
    assert string_utils.contains(string, symbol) is expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "U", False),
    ("SkyPro", "z", False),
    ("", "S", False),
    ("Тест", "X", False),
])
def test_contains_negative(string, symbol, expected):
    assert string_utils.contains(string, symbol) is expected


# ============================================================
#  delete_symbol
# ============================================================

@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("123", "2", "13"),
    ("04 апреля 2023", " ", "04апреля2023"),
])
def test_delete_symbol_positive(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "X", "SkyPro"),
    ("", "a", ""),
    (" ", " ", ""),
    ("Тест", "X", "Тест"),
])
def test_delete_symbol_negative(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected
