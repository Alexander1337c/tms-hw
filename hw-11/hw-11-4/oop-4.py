class Sphere:
    def __init__(self, rad=1, x=0, y=0, z=0):
        self.rad = rad
        self.x = x
        self.y = y
        self.z = z

    def get_volume(self):
        v = (4 / 3) * 3.14 * self.rad ** 3
        return v

    def get_square(self):
        s = 3.14 * 4 * self.rad ** 2
        return s

    def get_radius(self):
        return self.rad

    def get_center(self):
        return self.x, self.y, self.z

    def set_radius(self, rad):
        self.rad = rad

    def set_center(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def is_point_inside(self, x, y, z):
        if x ** 2 + y ** 2 + z ** 2 > self.rad ** 2:
            return False
        else:
            return True


shape = Sphere(6, 1, 2, 1)
print(shape.get_center())