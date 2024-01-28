class Calculator:
    def set_strategy(self, strategy):
        self.strategy = strategy

    def calculate(self, a, b):
        return self.strategy.execute(a, b)


class Addition:
    def execute(self, a, b):
        return a + b


class Substraction:
    def execute(self, a, b):
        return a - b


class Multiplication:
    def execute(self, a, b):
        return a * b


class Division:

    def execute(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError('Не число')
        if a == 0 or b == 0:
            raise ZeroDivisionError('Деление на ноль запрещено')
        return a / b


calc = Calculator()
calc.set_strategy(Division())
print(calc.calculate(3, '5'))
