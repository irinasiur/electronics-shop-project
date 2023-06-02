"""Здесь надо написать тесты с использованием pytest для модуля item."""
import sys
from io import StringIO

from src.item import Item
import pytest


    # TastCase #1 Calculate_Total_Price
def test_calculate_total_price():
    item11 = Item('bag', 900, 10)
    assert item11.calculate_total_price() == 9000
    item2 = Item('doll', 50.50, 10)
    assert item2.calculate_total_price() == 505.0
    item3 = Item('cat', 100, 0)
    assert item3.calculate_total_price() == 0


# TastCase #2 Apply_Discount
def test_apply_discount() -> None:
    item10 = Item('bag', 900, 10)
    assert item10.apply_discount() is None


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5
    item1 = Item.all[0]
    assert item1.name == 'Смартфон'


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_name():
    item7 = Item('cat', 100, 0)
    item7.name = "ne_cat"
    assert item7.name == "ne_cat"
    item7.name = 'СуперСмартфон'
    assert item7.name == "ne_cat"

