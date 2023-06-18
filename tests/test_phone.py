import pytest
from src.phone import Phone

@pytest.fixture
def one_phone():
    return Phone('Булкафон', 300, 10, 2)


def test_phone_init(one_phone):
    assert one_phone.name == 'Булкафон'
    assert one_phone.price == 300
    assert one_phone.quantity == 10
    assert one_phone.number_of_sim == 2


def test_phone_repr(one_phone):
    assert repr(one_phone) == "Phone('Булкафон', 300, 10, 2)"


def test_phone_number_of_sim(one_phone):
    one_phone.number_of_sim = 4
    assert one_phone.number_of_sim == 4
    with pytest.raises(ValueError):
        one_phone.number_of_sim = 0


