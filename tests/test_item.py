"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

if __name__ == '__main__':
    item1 = Item('bag', 900, 10)


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
