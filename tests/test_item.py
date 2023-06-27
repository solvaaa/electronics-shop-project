"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item, InstantiateCSVError

@pytest.fixture
def one_item():
    return Item('Булка', 40, 7)


def test_item_init(one_item):
    assert one_item.name == 'Булка'


def test_item_apply_discount(one_item):
    one_item.pay_rate = 0.5
    one_item.apply_discount()
    assert one_item.price == 20


def test_item_calculate_total_price(one_item):
    assert one_item.calculate_total_price() == 280


def test_item_name(one_item):
    one_item.name = 'Хлеб'
    assert one_item.name == 'Хлеб'


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
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv('./items.csv')
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv('../tests/failed_items.csv')

def test_item_repr(one_item):
    assert repr(one_item) == "Item('Булка', 40, 7)"


def test_item_str(one_item):
    assert str(one_item) == 'Булка'


@pytest.fixture
def second_item():
    return Item('Пирожок', 100, 6)


def test_item_add(one_item, second_item):
    assert one_item + second_item == 13
    with pytest.raises(TypeError):
        one_item + 8


