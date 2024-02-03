class BzzElephant:

    def __init__(self, bzz, elph):
        self.bzz = bzz
        self.elph = elph

    def fly(self):
        return True if self.bzz >= self.elph else False

    def trumpet(self):
        return f'wzzzz' if self.bzz <= self.elph else f'tu-tu-doo-doo'

    @property
    def eat(self):
        return self

    @eat.setter
    def eat(self, meal_value):
        meal, value = meal_value
        if meal == 'nectar':
            self.elph -= value
            self.bzz += value
            print('if')
        elif meal == 'grass':
            self.elph += value
            self.bzz -= value
            print('else')
        if self.bzz > 100:
            self.bzz = 100
            print('else')
        elif self.elph > 100:
            self.elph = 100
            print('else')
        self.bzz = 0 if self.bzz < 0 else self.bzz
        self.elph = 0 if self.elph < 0 else self.elph

    @eat.getter
    def eat(self):
        return f'{self.bzz, self.elph}'


bzzzz = BzzElephant(13, 15)
print(bzzzz.fly())
print(bzzzz.trumpet())
bzzzz.eat = 'nectar', 10
# bzzzz.eat = 'nectar', 10
# bzzzz.eat_bz = 'grass', 7
print(bzzzz.eat)
