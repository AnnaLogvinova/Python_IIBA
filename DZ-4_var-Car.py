#Создайте класс и поля соответствующему вашему варианту
# (поля статические и динамические).
# Создайте три метода (класса, объекта и статический).
# Выберете поле или метод для реализации инкапсуляции.
# Пропишите запись и считывание (get, set) инкапсулированных полей.
# Вар.5 Kласс Car:
# id, Марка, Модель, Год выпуска, Цвет, Цена, Регистрационный номер

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
        self.id_car = id
        self.brand_car = brand
        self.model_car = model
        self.year_car = year
        self.color_car = color
        self.price_car = price
        self.number_car = number
        # print('New object created!')

    def get_id(self):
        return self.id_car

    def get_brand(self):
        return self.brand_car

    def get_model(self):
        return self.model_car

    def get_year(self):
        return self.year_car

    def get_color(self):
        return self.color_car

    def get_price(self):
        return self.price_car

    def get_number(self):
        return self.number_car

    def car_age(self, curr_year=2022):
        return curr_year - self.get_year()

def info(item):
    print('---------------')
    print(f'Марка автомобиля: {Allthecars[item].get_brand()}')
    print(f'Модель автомобиля {Allthecars[item].get_model()}')
    print(f'Возраст автомобиля: {str(Allthecars[item].car_age())} years')
    print(f'Цвет автомобиля {Allthecars[item].get_color()}')
    print(f'Стоимость автомобиля: {str(Allthecars[item].get_price())} EURO')
    print('---------------')


Allthecars = [Car('stock_0', 'Maserati', 'Ghibli', 2021, 'grey', 3000000, '01456321'),
                  Car('stock_1', 'Lambargini', 'Diablo', 2007, 'black', 3000000, '01456322'),
                  Car('stock_2', 'Bugatti', 'Chiron', 2000, 'blue', 3000000, '01456323'),
                  Car('stock_3', 'BMW', 'X7', 2019, 'red', 100000, '01456324'),
                  Car('stock_4', 'Mercedes', 'CLS', 2017, 'grey', 100000, '01456325'),
                  Car('stock_5', 'Audi', 'Q7', 2013, 'blue', 100000, '01456326'),
                  Car('stock_6', 'Peugeot', '407', 2017, 'grey', 25000, '01459321'),
                  Car('stock_7', 'Nissan', 'Patrol', 2000, 'grey', 25000, '01476321'),
                  Car('stock_8', 'Porsche', '911', 2009, 'black', 100000, '01456421'),
                  Car('stock_9', 'Ferrari', 'Testarossa', 2021, 'red', 3000000, '02456321'),
                  Car('stock_10', 'Volkswagen', 'Golf', 2000, 'black', 25000, '01456821'),
                  Car('stock_11', 'Honda', 'Civic', 2008, 'red', 25000, '01456331'),
                  Car('stock_12', 'Toyota', 'Camry', 2001, 'grey', 25000, '01456521'),
                  Car('stock_13', 'Dodge', 'Caravan', 2020, 'red', 25000, '01459321'),
                  Car('stock_14', 'Ford', 'Mustang', 2000, 'red', 25000, '01456921'),
                  Car('stock_15', 'Opel', 'Corsa', 2020, 'blue', 25000, '01456329')]

def search_price_car(p):
    for i in range(len(Allthecars)):
        if Allthecars[i].get_price() == p:
            info(i)

def search_color_car(c):
    for i in range(len(Allthecars)):
        if Allthecars[i].get_color() == c:
            info(i)

p_s = (int(input('Выберите стоимость автомобиля: 3000000, 100000, 25000  \n')))
search_price_car(p_s)

c_s = (input('Выберите цвет black or red or grey or blue \n'))
search_color_car(c_s)

