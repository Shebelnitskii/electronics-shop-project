"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
import unittest
from src.item import Item

@pytest.fixture()
def item():
    return Item('Мышь',1500,1)

@pytest.fixture()
def item1():
    return Item('Клавиатура',2000,5)

def test_calculate_total_price(item):
    assert item.calculate_total_price() == 1500

def test_apply_discount(item):
    assert item.apply_discount() == None

def test_name(item):
    assert item.name == "Мышь"

def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    item = Item.all[0]
    assert item.name == "Смартфон"

def test_string_to_number():
    assert Item.string_to_number("1000") == 1000
    assert Item.string_to_number("1000.00") == 1000

def test_setter_name(item):
    item.name = "Монитор"
    assert item.name == "Монитор"
    item.name = "Клавиатура"
    assert item.name == "Клавиатура"

def test_repr(item):
    assert repr(item) == "Item('Мышь', 1500, 1)"

def test_str(item):
    assert str(item) == 'Мышь'

def test_add(item,item1):
    assert item + item1 == 6




