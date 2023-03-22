import pytest
from src.phone import Phone,Item

@pytest.fixture
def phone():
    return Phone("iPhone 14", 120_000, 5, 2)

@pytest.fixture
def item():
    return Item('Мышь',1500,4)

def test_calculate_total_price(phone):
    assert phone.calculate_total_price() == 600000

def test_name(phone):
    assert phone.name == "iPhone 14"

def test_apply_discount(phone):
    assert phone.apply_discount() == None

def test_instantiate_from_csv():
    Phone.instantiate_from_csv()
    phone = Phone.all[0]
    assert phone.name == "Смартфон"

def test_string_to_number():
    assert Phone.string_to_number("1000") == 1000
    assert Phone.string_to_number("1000.00") == 1000

def test_setter_name(phone):
    phone.name = "Монитор"
    assert phone.name == "Монитор"
    phone.name = "Клавиатура"
    assert phone.name == "Клавиатура"

def test_repr(phone):
    assert repr(phone) == "Phone('iPhone 14', 120000, 5, 2)"

def test_add(item, phone):
    assert item + phone == 9

def test_add_phone(phone):
    assert phone + phone == 10