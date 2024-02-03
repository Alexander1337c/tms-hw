class Bus:
    def __init__(self, speed=0, max_seats=0, max_speed=0, list_of_passenger=None, flag_seats=False, dict_seats=None):
        if list_of_passenger is None:
            self.__list_of_passenger = []
        if dict_seats is None:
            self.__dict_seats = {}
        self.__speed = speed
        self.__max_seats = max_seats
        self.__max_speed = max_speed
        self.__flag_seats = flag_seats

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed):
        self.__speed = speed

    @property
    def max_speed(self):
        return self.__max_speed

    @max_speed.setter
    def max_speed(self, max_speed):
        self.__max_speed = max_speed

    @property
    def max_seats(self):
        return self.__max_seats

    @max_seats.setter
    def max_seats(self, max_seats):
        self.__max_seats = max_seats

    @property
    def list_passenger(self):
        return self.__list_of_passenger

    @list_passenger.setter
    def list_passenger(self, list_passenger):
        self.__list_of_passenger = list(list_passenger)

    @property
    def flag_seats(self):
        return self.__flag_seats

    @flag_seats.setter
    def flag_seats(self, flag):
        self.__flag_seats = flag

    @property
    def dict_seats(self):
        return self.__dict_seats

    @dict_seats.setter
    def dict_seats(self, dict_seats):
        self.__dict_seats = dict_seats

    def increase_speed(self, speed):
        self.__speed += speed

    def decrease_speed(self, speed):
        self.__speed -= speed

    def change_dict(self):
        len_pass = len(self.__list_of_passenger)
        self.__dict_seats = {}
        for i in range(len_pass):
            self.__dict_seats[i + 1] = self.__list_of_passenger[i]

    def increase_passenger(self, passenger):
        self.__list_of_passenger += passenger
        self.change_dict()

    def decrease_passenger(self, passenger):
        for i in passenger:
            if i in self.__list_of_passenger:
                self.__list_of_passenger.remove(i)
        self.change_dict()

    def landing_passenger_last_name(self, passengers):
        self.__list_of_passenger += list(passengers)
        self.change_dict()

    def unlanding_passenger_last_name(self, passenger):
        if passenger in self.__list_of_passenger:
            self.__list_of_passenger.remove(passenger)
            self.change_dict()
        else:
            raise ValueError('Такого пассажира нет')


a = Bus()
a.speed = 90
print(a.speed)
a.decrease_speed(30)
print(a.speed)
a.list_passenger = 'Kolas', 'Vishnev', 'Zohan'
print(a.list_passenger)
print(a.list_passenger)
a.landing_passenger_last_name(['Chopikov', 'Nazarov'])
print(a.list_passenger)
a.unlanding_passenger_last_name('Chopikov')
a.increase_passenger(['Mosak', 'Farad'])
print(a.list_passenger)
a.decrease_passenger(['Farad', 'Mosak'])
print(a.list_passenger)
print(a.dict_seats)
