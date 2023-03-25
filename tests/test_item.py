"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
import unittest
from src.item import Item

@pytest.fixture()
def keyboard():
    return Item('Мышь',1500,1)

@pytest.fixture()
def item1():
    return Item('Клавиатура',2000,5)

def test_calculate_total_price(keyboard):
    assert keyboard.calculate_total_price() == 1500

def test_apply_discount(keyboard):
    assert keyboard.apply_discount() == None

def test_name(keyboard):
    assert keyboard.name == "Мышь"

def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    item = Item.all[0]
    assert item.name == "Смартфон"

def test_string_to_number():
    assert Item.string_to_number("1000") == 1000
    assert Item.string_to_number("1000.00") == 1000

def test_setter_name(keyboard):
    keyboard.name = "Монитор"
    assert keyboard.name == "Монитор"
    keyboard.name = "Клавиатура"
    assert keyboard.name == "Клавиатура"

def test_repr(keyboard):
    assert repr(keyboard) == "Item('Мышь', 1500, 1)"

def test_str(keyboard):
    assert str(keyboard) == 'Мышь'

def test_add(keyboard, item1):
    assert keyboard + item1 == 6




