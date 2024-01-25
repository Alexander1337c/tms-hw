class Math:
    def __int__(self):
        pass

    def is_number(self, a, b):
        if isinstance(a, int) and isinstance(b, int):
            return True
        else:
            return 'Не число'
    def addition(self, a, b):
        if self.is_number(a, b):
            print(a + b)

    def substraction(self, a, b):
        if self.is_number(a, b):
            print(a - b)

    def multiplication(self, a, b):
        if self.is_number(a, b):
            print(a * b)

    def division(self, a, b):
        if a == 0 or b == 0:
            print("Деление на 0 запрещено")
        else:
            if self.is_number(a, b):
                print(a / b)


action = Math()
action.division(3, 3)
