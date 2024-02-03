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
        self.reset()

    def reset(self):
        self._pizza = Pizza()

    @property
    def pizza(self):
        pizza = self._pizza
        self.reset()
        return pizza

    def set_size(self, size=0):
        self._pizza.size = size
        return self

    def set_cheese(self, cheese=0):
        self._pizza.cheese = cheese
        return self

    def set_pepperoni(self, pepperoni=0):
        self._pizza.pepperoni = pepperoni
        return self

    def set_mushrooms(self, mushrooms=0):
        self._pizza.mushrooms = mushrooms
        return self

    def set_onions(self, onions=0):
        self._pizza.onions = onions
        return self

    def set_bacon(self, bacon=0):
        self._pizza.bacon = bacon
        return self

    def get_pizza(self):
        parts = []
        for i in self._pizza.__dict__.values():
            if i is not None:
                parts.append(i)
        print(parts)
        return self._pizza


class PizzaDirector:

    def __init__(self):
        self._builder = None

    @property
    def builder(self):
        return self._builder

    @builder.setter
    def builder(self, builder):
        self._builder = builder

    def make_pizza_one_option(self):
        self.builder.set_size(32)
        self.builder.set_cheese('Add cheese')
        self.builder.set_pepperoni('Add pepperoni')
        self.builder.get_pizza()

    def make_pizza_second_option(self):
        self.builder.set_size(26)
        self.builder.set_mushrooms('Add mushrooms')
        self.builder.set_onions('Add onions')
        self.builder.set_bacon('Add bacon')
        self.builder.get_pizza()


director = PizzaDirector()
builder = PizzaBuilder()
director.builder = builder
director.make_pizza_second_option()
