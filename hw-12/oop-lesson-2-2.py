class BzzElephant:

    def __init__(self, bzz, elph):
        self.bzz = bzz
        self.elph = elph

    def fly(self):
        return True if self.bzz >= self.elph else False

    def trumpet(self):
        return f'wzzzz' if self.bzz <= self.elph else f'tu-tu-doo-doo'

    def eat(self, meal, value=0):
        if meal == 'nectar':
            self.elph -= value
            self.bzz += value
        elif meal == 'grass':
            self.elph += value
            self.bzz -= value
        if self.bzz > 100:
            self.bzz = 100
        elif self.elph > 100:
            self.elph = 100
        self.bzz = 0 if self.bzz < 0 else self.bzz
        self.elph = 0 if self.elph < 0 else self.elph
        return f'{self.bzz, self.elph}'


bzzzz = BzzElephant(13, 15)
print(bzzzz.bzz, bzzzz.elph)
print(bzzzz.fly())
print(bzzzz.trumpet())
print(bzzzz.eat('nectar', 10))
print(bzzzz.eat('nectar', 10))
print(bzzzz.eat('grass', 7))
