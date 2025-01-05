class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white'] # список допустимых цветов для окрашивания

    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = str(owner) # владелец транспорта
        self.__model = str(__model) # модель (марка) транспорта
        self.__color = str(__color) # название цвета
        self.__engine_power = int(__engine_power) # мощность двигателя


    def get_model(self, __model):
        # возвращает строку: "Модель: <название модели транспорта>"
        print(f'Модель: {self.__model}')

    def get_horsepower(self, __engine_power):
        # возвращает строку: "Мощность двигателя: <мощность>"
        print(f'Мощность двигателя: {self.__engine_power}')

    def get_color(self, __color):
        # возвращает строку: "Цвет: <цвет транспорта>"
        print(f'Цвет: {self.__color}')

    def print_info(self):
        # распечатывает результаты методов (в том же порядке): get_model, get_horsepower, get_color; а так же
        # владельца в конце в формате "Владелец: <имя>"
        self.get_model(self)
        self.get_horsepower(self)
        self.get_color(self)
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color):
        # принимает аргумент new_color(str), меняет цвет __color на new_color, если он есть в списке __COLOR_VARIANTS,
        # в противном случае выводит на экран надпись: "Нельзя сменить цвет на <новый цвет>"
        for i in self.__COLOR_VARIANTS:
            if new_color.lower() == i:
                self.__color = new_color
                return
        print(f'Нельзя сменить цвет на {new_color}')

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5 # в седан может поместиться только 5 пассажиров

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()