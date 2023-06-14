from src.keyboard import Keyboard, MixinLog
#from src.item import Item


def test_language():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert str(kb) == "Dark Project KD87A"
    assert str(kb.language) == "EN"
    kb.language = 'CH'
    assert "AttributeError: property 'language' of 'KeyBoard' object has no setter"
    kb.language = 'RU'
    assert str(kb.language) == "EN"

def test_change_lang():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    kb.change_lang()
    assert str(kb.language) == "RU"
    kb.change_lang().change_lang()
    assert str(kb.language) == "RU"