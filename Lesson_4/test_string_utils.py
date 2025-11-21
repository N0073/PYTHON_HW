from string_utils import StringUtils
import pytest

string_utils = StringUtils()

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("natalia", "Natalia"),
    ("natalia savina", "Natalia savina"),
    ("04 апреля 2023", "04 апреля 2023"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("  " , "  "),
    ("", ""),
    ("123","123"),
])
def test_capitalize_negative(input_str, expected):
       assert string_utils.capitalize(input_str) == expected




@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("  hello World", "hello World"),  # пробелы по краям
    (" noSpaces", "noSpaces"),  # строка без пробелов
    ("", ""),  # только пробелы, должна вернуться пустая строка
    (" 123", "123"),  #цифровые значения

])

def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("hello", "hello"),  # отстутствие пробелов по краям
    ("123456 ", "123456 "),  # только пробелы, должна вернуться пустая строка
    ("", ""),  #пустая строка
    ])
def test_trim_negative(input_str, expected):
        assert string_utils.trim(input_str) == expected




@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Hello", "H", True),  # символ 'H' есть в строке "Hello"
    ("Test", "T", True),   # символа 'Т' нет в строке "Test"
    ("123", "2", True),        #искомые цифры
])
def test_contains_positive(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Hello", "S", False),  # символа 'S' нет в строке "Hello"
    ("Test", "O", False),  # символа 'O' нет в строке "Test"
    ("123", "P", False), #символа 'P' нет в строке "123"
])

def test_contains_negative(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected



@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
  ("banana", "a", "bnn"), #символ "a" удаляется, остается "bnn"
    ("banana", "x", "banana"),  # символ "x" не найден, строка остается без изменений.
    ("", "a", ""),  # пустая строка остается пустой
    ("test", "", "test"),  #  пустой символ не влияет на строку.
])
def test_delete_symbol_positive(string, symbol, expected):
    utils = StringUtils()
    result = utils.delete_symbol(string, symbol)
    assert result == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("banana", "", "banana"),  # невалидный символ
    ("", "a", ""),  # невалидная строка
])
def test_delete_symbol_negative(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected























