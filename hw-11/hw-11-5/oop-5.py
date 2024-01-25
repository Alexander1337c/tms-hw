class SuperStr:
    def __init__(self, s):
        self.s = s

    def is_repeatance(self, s):
        res = len(self.s) % len(s)
        return f'True' if res == 0 else f'False'

    def is_palindrome(self):
        print(f'Строка {self.s} является палиндромом') if (self.s.lower() ==
                                                           self.s[::-1].lower() or not self.s) else print(
            'Не палиндром')


sup = SuperStr('abccba')
sup.is_palindrome()
