class Pizza:
    def __init__(self):
        self.size = None
        self.cheese = None
        self.pepperoni = None
        self.mushrooms = None
        self.onions = None
        self.bacon = None


class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def set_size(self, size=0):
        self.pizza.size = size
        return self

    def set_cheese(self, cheese=0):
        self.pizza.cheese = cheese
        return self

    def set_pepperoni(self, pepperoni=0):
        self.pizza.pepperoni = pepperoni
        return self

    def set_mushrooms(self, mushrooms=0):
        self.pizza.mushrooms = mushrooms
        return self

    def set_onions(self, onions=0):
        self.pizza.onions = onions
        return self

    def set_bacon(self, bacon=0):
        self.pizza.bacon = bacon
        return self

    def get_pizza(self):
        print(self.pizza.__dict__)

class PizzaDirector:

    def __init__(self):
        self._builder = None

    @property
    def builder(self):
        return self._builder

    @builder.setter
    def builder(self, builder):
        self._builder = builder

    def make_pizza(self):
        self.builder.set_size()
        self.builder.set_cheese()
        self.builder.set_pepperoni()
        self.builder.set_mushrooms()
        self.builder.set_onions()
        self.builder.set_bacon()
        self.builder.get_pizza()


director = PizzaDirector()
builder = PizzaBuilder()
director.builder = builder
director.make_pizza()
