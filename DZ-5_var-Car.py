# Создайте класс и поля соответствующему вашему варианту
# (поля статические и динамические).
# Создайте три метода (класса, объекта и статический).
# Выберете поле или метод для реализации инкапсуляции.
# Пропишите запись и считывание (get, set) инкапсулированных полей.
# Вар.5 Kласс Car:
# id, Марка, Модель, Год выпуска, Цвет, Цена, Регистрационный номер
# ДОБАВИТЬ 2-3 МАГИЧЕСКИХ МЕТОДОВ

class Car:
    # Статические поля
    default_id = ''
    default_brand = 'No name'
    default_model = 'No model'
    default_year = ''
    default_color = ' No color'
    default_price = ''
    default_number = 'No number'

    def __init__(self, id, brand, model, year, color, price, number):
        self.__id = id
        self.__brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.price = price
        self.number = number
        # print('New object created!')

    # методы класса

    def set_id(self):
        id = 'stock_a'
        while not id.isnumeric():
            id = input('Изменить id: ')
        self.__id = id
        return print("Теперь id стало" + self.__id)

    def set_brand(self):
        brand = input('Brand: ')
        self.__brand = brand
        return self.__brand

    def set_model(self, model):
        self.model = model

    def set_year(self):
        year = 'yyyy'
        while not year.isnumeric():
            year = input('year: ')
        self.year = year
        return self.year

    def set_color(self, color):
        self.color = color

    def set_price(self, price):
        self.price = price

    def set_number(self, number):
        self.number = number

    def get_id(self):
        return self.id

    def get_brand(self):
        return str(self.__brand)

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_color(self):
        return str(self.color)

    def get_price(self, price):
        return str(self.price)

    def get_number(self):
        return self.number

    def car_age(self, curr_year=2022):
        return curr_year - self.get_year()

    # статический метод
    @staticmethod
    def getCar():
        return "Used Car"

    # метод класса
    @classmethod
    def color(cls, __brand, model, year, price, number):
        color = cls("black", model, year, price, number)
        return print("Цвет " + color)

    # магические методы
    def __str__(self):
        return f'Автомобиль "{self.__brand}", цвета {self.color} {self.year} года.'

    def __repr__(self):
        return f"Car({self.__id!r}, {self.__brand!r}, {self.color!r}, {self.model!r}, {self.year!r}, {self.price!r}, {self.number!r})"

    def __getitem__(self, color):
        return self.color

    def __mull__(self, price):
        return price * 2.5


print("Введите 3 автомобиля: ")

num1_brand = str(input("Введите марку: "))
num1_model = str(input("Введите модель: "))
num1_year = int(input("Введите год: "))
num1_color = str(input("Введите цвет: "))
num1_price = int(input("Введите стоимость: "))
num1_number = str(input("Введите номер: "))
print('---------------------')

num2_brand = str(input("Введите марку: "))
num2_model = str(input("Введите модель: "))
num2_year = int(input("Введите год: "))
num2_color = str(input("Введите цвет: "))
num2_price = int(input("Введите стоимость: "))
num2_number = str(input("Введите номер: "))
print('---------------------')

num3_brand = str(input("Введите марку: "))
num3_model = str(input("Введите модель: "))
num3_year = int(input("Введите год: "))
num3_color = str(input("Введите цвет: "))
num3_price = int(input("Введите стоимость: "))
num3_number = str(input("Введите номер: "))
print('---------------------')

list_of_b = list()
car_1 = Car(15, num1_brand, num1_model, num1_year, num1_color, num1_price, num1_number)
car_2 = Car(16, num2_brand, num2_model, num2_year, num2_color, num2_price, num2_number)
car_3 = Car(17, num3_brand, num3_model, num3_year, num3_color, num3_price, num3_number)
car_4 = Car(18, 'Lada', "7", 2010, "white", 1000, "7070A")

list_of_b.append(car_1)
list_of_b.append(car_2)
list_of_b.append(car_3)
list_of_b.append(car_4)

#new_list = []
#search1 = str(input('Поиск по цвету: '))
#for car in list_of_b:
#    if Car.get_color(car) == search1:
#        new_list.append(car)
#for book in new_list:
#    print(Car.get_brand(car))

#new_list_2 = []
#search2 = int(input('Поиск по году: '))
#for book in list_of_b:
#    if Car.get_year(car) == search2:
#        new_list_2.append(car)
#for book in new_list_2:
#    print(Car.get_brand(car))

print("======================")
print("Информация через __str__")
print(car_1)
print(car_2)
print(car_3)
print(car_4)
print("======================")
print("Информация через __repr__")
print(repr(list_of_b))

print("======================")
print("Цвета автомобилей: ")
print(car_1.__getitem__(color=num1_color))
print(car_2.__getitem__(color=num2_color))
print(car_3.__getitem__(color=num3_color))
print(car_4.__getitem__(color="white"))

print("======================")
print("Стоимость в рублях: ")
print(car_1.__mull__(price=num1_price))
print(car_2.__mull__(price=num2_price))
print(car_3.__mull__(price=num3_price))
print(car_4.__mull__(price=1000))
