class Sphere:
    def __init__(self, rad=1, x=0, y=0, z=0):
        self.rad = rad
        self.x = x
        self.y = y
        self.z = z

    def get_volume(self):
        v = (4 / 3) * 3.14 * self.rad ** 3
        print(f"Объем шара {v:.2f} см3")

    def get_square(self):
        s = 3.14 * 4 * self.rad ** 2
        print(f'Площадь поверхности {s}')

    def get_radius(self):
        print(f'Радиус текущей сферы {self.rad}')

    def get_center(self):
        print(f'Координаты центра окружности {(self.x, self.y, self.z)}')

    def set_radius(self, rad):
        self.rad = rad

    def set_center(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def is_point_inside(self, x, y, z):
        if x ** 2 + y ** 2 + z ** 2 > self.rad ** 2:
            print(False)
        else:
            print(True)


shape = Sphere(6, 1, 2, 1)
