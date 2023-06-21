import pytest
from src.keyboard import Keyboard


@pytest.fixture
def keyboard():
    return Keyboard('Dark Project KD87A', 9600, 5)

def test_keyboard_init(keyboard):
    assert str(keyboard) == "Dark Project KD87A"
    assert keyboard.language == "EN"
    with pytest.raises(AttributeError):
        keyboard.language = "FR"

def test_keyboard_change_lang(keyboard):
    keyboard.change_lang()
    assert keyboard.language == "RU"
    keyboard.change_lang().change_lang()
    assert keyboard.language == "RU"

