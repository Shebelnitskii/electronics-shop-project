import pytest
from src.keyboard import KeyBoard

@pytest.fixture
def keyboard():
    return KeyBoard('Dark Project KD87A', 9600, 5)

def test_change_lang(keyboard):
    assert keyboard.language == 'EN'
    keyboard.change_lang()
    assert keyboard.language == 'RU'
    keyboard.change_lang()
    assert keyboard.language == 'EN'

def test_calculate_total_price(keyboard):
    assert keyboard.calculate_total_price() == 48000

def test_apply_discount(keyboard):
    assert keyboard.apply_discount() == None

def test_name(keyboard):
    assert keyboard.name == "Dark Project KD87A"


def test_string_to_number():
    assert KeyBoard.string_to_number("1000") == 1000
    assert KeyBoard.string_to_number("1000.00") == 1000

def test_setter_name(keyboard):
    keyboard.name = "Монитор"
    assert keyboard.name == "Монитор"
    keyboard.name = "Клавиатура"
    assert keyboard.name == "Клавиатура"


def test_str(keyboard):
    assert str(keyboard) == 'Dark Project KD87A'


