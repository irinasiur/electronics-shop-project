from item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity, number_of_sim)
        self.number_of_sim = number_of_sim

    def __add__(self, other):
        """
        Складывет экземпляры класса Phone и Item (количество товара в магазине).
        """
        if not issubclass(Phone, Item):
            return NotImplemented
        if not isinstance(other, Phone):
            return NotImplemented
        return int(self.quantity) + int(other.quantity)
