"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


def one_item():
    return Item('Булка', 40, 7)


def test_item_init():
    bread = one_item()
    assert bread.name == 'Булка'


def test_item_apply_discount():
    bread = one_item()
    bread.pay_rate = 0.5
    bread.apply_discount()
    assert bread.price == 20


def test_item_calculate_total_price():
    bread = one_item()
    assert bread.calculate_total_price() == 280


def test_item_name():
    bread = one_item()
    bread.name = 'Хлеб'
    assert bread.name == 'Хлеб'


def test_item_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_item_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5  # в файле 5 записей с данными по товарам
    item1 = Item.all[0]
    assert item1.name == 'Смартфон'
    Item.all.clear()

