"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item

@pytest.fixture()
def name():
    return Item(0,0,0)

def test_calculate_total_price(name):
    assert name.calculate_total_price() == 0.0

def test_apply_discount(name):
    assert name.apply_discount() == None