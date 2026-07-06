import pytest

from string_utils import StringUtils

string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    (" Skypro", "Skypro"),
    (" Hello world", "Hello world"),
    ("Python ", "Python "),
])
def test_trim_positive(string_utils, input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("invalid_input", [
    123,
    None,
])
def test_trim_negative(string_utils, invalid_input):
    with pytest.raises(AttributeError):
        string_utils.trim(invalid_input)


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "S", True),
    ("SkyPro", "U", False),
    ("SkyPro", "o", True),
    ("SkyPro", "y", True),
    ("SkyPro", "s", False),
])
def test_contains_positive(string_utils, input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("invalid_str, invalid_symbol", [
    (12345, "1"),
    ("SkyPro", 9),
    (None, "S"),
    ("SkyPro", None),
    (["SkyPro"], "S"),
])
def test_contains_negative(string_utils, invalid_str, invalid_symbol):
    with pytest.raises((TypeError, AttributeError)):
        string_utils.contains(invalid_str, invalid_symbol)


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("SkyPro", "U", "SkyPro"),
    ("banana", "a", "bnn"),
    ("SkyPro", "sky", "SkyPro"),
])
def test_delete_symbol_positive(string_utils, input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("invalid_str, invalid_symbol", [
    (12345, "1"),
    ("SkyPro", 9),
    (None, "k"),
])
def test_delete_symbol_negative(string_utils, invalid_str, invalid_symbol):
    with pytest.raises((TypeError, AttributeError)):
        string_utils.delete_symbol(invalid_str, invalid_symbol)
