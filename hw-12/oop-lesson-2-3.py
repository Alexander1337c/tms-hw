class Bus:
    def __init__(self, speed=0, max_seats=0, max_speed=0, list_of_passenger=None, flag_seats=False, dict_seats=None):
        if list_of_passenger is None:
            self.list_of_passenger = []
        if dict_seats is None:
            self.dict_seats = {}
        self.speed = speed
        self.max_seats = max_seats
        self.max_speed = max_speed
        self.flag_seats = flag_seats

    def get_speed(self):
        return self.speed

    def set_speed(self, speed):
        self.speed = speed

    def get_max_speed(self):
        return self.max_speed

    def set_max_speed(self, max_speed):
        self.max_speed = max_speed

    def get_max_seats(self):
        return self.max_seats

    def set_max_seats(self, max_seats):
        self.max_seats = max_seats

    def get_list_passenger(self):
        return self.list_of_passenger

    def set_list_passenger(self, list_passenger):
        self.list_of_passenger = list(list_passenger)

    def get_flag_seats(self):
        return self.flag_seats

    def set_flag_seats(self, flag):
        self.flag_seats = flag

    def get_dict_seats(self):
        return self.dict_seats

    def set_dict_seats(self, dict_seats):
        self.dict_seats = dict_seats

    speed_bus = property(get_speed, set_speed)
    max_speed_bus = property(get_max_speed, set_max_speed)
    max_seats_bus = property(get_max_seats, set_max_seats)
    list_passenger = property(get_list_passenger, set_list_passenger)
    flag_seats_bus = property(get_flag_seats, set_flag_seats)
    dict_seats_bus = property(get_dict_seats, set_dict_seats)

    def increase_speed(self, speed):
        self.speed += speed

    def decrease_speed(self, speed):
        self.speed -= speed

    def increase_passenger(self, passenger):
        self.list_of_passenger += passenger

    def decrease_passenger(self, passenger):
        for i in passenger:
            if i in self.list_of_passenger:
                self.list_of_passenger.remove(i)

    def landing_passenger_last_name(self, passengers):
        self.list_of_passenger += list(passengers)

    def unlanding_passenger_last_name(self, passenger):
        if passenger in self.list_of_passenger:
            self.list_of_passenger.remove(passenger)
        else:
            return f'Такого пассажира нет'


a = Bus()
a.speed_bus = 90
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
