class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year
        print(f'Создался автомобиль цвета {self.color}')

    def start_car(self):
        print(f'Автомобиль заведен')

    def stop_car(self):
        print(f'Автомобиль заглушен')

    def add_color(self, color):
        self.color = color

    def add_type(self, type):
        self.type = type

    def add_year(self, year):
        self.year = year


bmw = Car('Green', 'Cupe', 1998)
bmw.start_car()
bmw.stop_car()

bmw.color = 'Red'
print(bmw.color)
bmw.year = 1966
print(bmw.year)
