import csv

PATH = '../src/items.csv'
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

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        cost = self.price * self.quantity
        return cost

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        discount = self.price * self.pay_rate
        self.price = discount

    @property
    def name(self):
        return f'{self.__name}'

    @name.setter
    def name(self, name):
        if len(name) <= 10:
            self.__name = name
        else:
            raise Exception("Длина наименования товара превышает 10 символов")

    @classmethod
    def instantiate_from_csv(cls, path=PATH):
        '''
        Создаёт новые экземпляры класса из csv файла
        '''
        try:
            opened_file = open(path, 'r', newline='', encoding='windows-1251')
        except FileNotFoundError as e:
            raise FileNotFoundError('Отсутствует файл items.csv') from e
        else:
            with opened_file as csvfile:
                try:
                    read_file = csv.DictReader(csvfile)
                    for items in read_file:
                        name = items['name']
                        price = cls.string_to_number(items['price'])
                        quantity = float((items['quantity']))
                        cls.all.append(cls(name, price, quantity))
                except Exception as e:
                    raise InstantiateCSVError from e

        return None

    @staticmethod
    def string_to_number(number_string):
        '''
        Возвращает int число из числа-строки
        '''
        return int(float(number_string))

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.__name}"

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            raise TypeError('Невозможно сложить класс с объектом другого класса')


class InstantiateCSVError(Exception):
    """
    Класс исключения для метода
    """
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Файл items.csv поврежден'

    def __str__(self):
        return self.message