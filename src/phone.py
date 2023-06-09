from src.item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        self.__number_of_sim = int(number_of_sim) if number_of_sim > 0 else "ValueError: Количество физических SIM-карт должно быть целым числом больше нуля."


    def __repr__(self):
        # "Item('Смартфон', 10000, 20)"
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.__number_of_sim})"

    @property
    def number_of_sim(self):
        """
        Геттер
        """
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, a):
        """
        Сеттер проверяет, что лоличество физических SIM-карт целое число и больше нуля.
        """
        if int(a) > 0:
            self.__number_of_sim = int(a)
        else:
            print("ValueError: Количество физических SIM-карт должно быть целым числом больше нуля.")

