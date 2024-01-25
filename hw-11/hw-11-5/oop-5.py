class SuperStr(str):

    def is_repeatance(self, s):
        res = len(self) % len(s)
        return f'True' if res == 0 else f'False'

    def is_palindrome(self):
        return self.lower() == self[::-1].lower()


sup = SuperStr('abccba')
print(sup.is_palindrome())
