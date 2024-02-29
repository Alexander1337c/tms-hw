class SuperStr(str):

    def is_repeatance(self, s):
        if not isinstance(s, str):
            return False
        res = len(self) // (len(s) or 1)
        return self == res*s

    def is_palindrome(self):
        return self.lower() == self[::-1].lower()


sup = SuperStr('abcabc')
# print(sup.is_palindrome())

print(sup.is_repeatance('abc'))