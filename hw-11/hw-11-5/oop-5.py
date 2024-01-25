class SuperStr(str):

    def is_repeatance(self, s):
        res = len(self) % len(s)
        return True if res == 0 else False

    def is_palindrome(self):
        return self.lower() == self[::-1].lower()


sup = SuperStr('abccba')
print(sup.is_palindrome())
