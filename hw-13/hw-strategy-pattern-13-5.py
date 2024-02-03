from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def execute(self, data_a, data_b):
        pass


class Calculator:

    def __init__(self):
        self.strategy = None

    def set_strategy(self, strategy):
        self.strategy = strategy

    def calculate(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError('NaN')
        return self.strategy.execute(a, b)


class Addition(Strategy):
    def execute(self, a, b):
        return a + b


class Substraction(Strategy):
    def execute(self, a, b):
        return a - b


class Multiplication(Strategy):
    def execute(self, a, b):
        return a * b


class Division(Strategy):

    def execute(self, a, b):
        if a == 0 or b == 0:
            raise ZeroDivisionError('Divizion by zero')
        return a / b


calc = Calculator()
calc.set_strategy(Multiplication())
print(calc.calculate(3, 7))
