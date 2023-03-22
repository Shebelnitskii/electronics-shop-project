import csv
import src

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
        self.__name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"Item('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.__name}'

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            return TypeError('Item')

    @property
    def name(self):
        return f'{self.__name}'

    @name.setter
    def name(self, name):
        if len(name) > 10:
            raise ValueError('Название товара должно содержать не более 10 символов.')
        self.__name = name


    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price*self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price*self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        """
        Создает экземпляр класса Item из файла csv.
        """
        with open('U:\PythonProjects\electronics-shop-project\src\items.csv') as f:
            reader = csv.DictReader(f, delimiter=',')
            for row in reader:
                item = Item(row['name'], row['price'], row['quantity'])
                cls.all.append(item)

    def string_to_number(self:str):
        """
        Преобразует строку в число.
        """
        return int(round(float(self),1))