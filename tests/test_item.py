"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item, InstantiateCSVError
import csv

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

def test_instantiate_from_csv():
    file_path = "U:/PythonProjects/electronics-shop-project/tests/test_items.csv"
    data = [
        {"name": "продукт№1", "price": "150", "quantity": "12"},
        {"name": "продукт№2", "price": "200.0", "quantity": "5"},
    ]
    with open(file_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "price", "quantity"])
        writer.writeheader()
        for row in data:
            writer.writerow(row)

    Item.instantiate_from_csv(file_path)

    assert len(Item.all) == 2
    assert Item.all[0].name == "продукт№1"
    assert Item.all[0].price == '150'
    assert Item.all[0].quantity == '12'
    assert Item.all[1].name == "продукт№2"
    assert Item.all[1].price == '200.0'
    assert Item.all[1].quantity == '5'


def test_instantiate_from_csv_file_not_found():
    file_path = '../tests/item.csv'
    with pytest.raises(FileNotFoundError, match="Отсутствует файл item.csv"):
        Item.instantiate_from_csv(file_path)

# def test_instantiate_from_csv_corrupted_file():
#     file_path = '../tests/test_items2.csv'
#     data = [
#         {"name": "Product1", "price": "100.0"},
#         {"name": "Product2", "quantity": "5"},
#     ]
#     with open(file_path, "w", newline="") as f:
#         writer = csv.DictWriter(f, fieldnames=["name", "price", "quantity"])
#         writer.writeheader()
#         for row in data:
#             writer.writerow(row)
#
#     with pytest.raises(InstantiateCSVError, match="Файл item.csv поврежден"):
#         Item.instantiate_from_csv(file_path)