import csv


# from src.phone import Phone


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    @classmethod
    def instantiate_from_csv(cls):
        """
        Инициализирует экземпляры класса `Item` данными из файла _src/items.csv.

        """
        cls.all.clear()
        filename = '/home/irinka/PycharmProjects/electronics-shop-project/src/items.csv'
        try:
            with open(filename, 'r', newline='', encoding='windows-1251') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    cls(row['name'], row['price'], row['quantity'])
        except FileNotFoundError:
            print('Файл не найден')

    @staticmethod
    def string_to_number(str):
        """
        Cтатический метод, возвращающий число из числа-строки.
        """
        return int(float(str))

    @property
    def name(self):
        """
        Геттер
        """
        return self.__name

    @name.setter
    def name(self, a):
        """
        Сеттер проверяет, что длина наименования товара не больше 10 симвовов.
        """
        if len(a) <= 10:
            self.__name = a
        else:
            print('Длина наименования товара превышает 10 символов')

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * Item.pay_rate

    def __repr__(self):
        # "Item('Смартфон', 10000, 20)"
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        """
        Возвращает название товара.
        """
        return f"{self.__name}"

    def __add__(self, other):
        """
        Складывет экземпляры класса Phone и Item (количество товара в магазине).
        """
        from src.phone import Phone
        if not issubclass(Phone, Item):
            return NotImplemented
        if not isinstance(other, Phone):
            return NotImplemented
        return int(self.quantity) + int(other.quantity)


