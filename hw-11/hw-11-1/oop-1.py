class Soda:
    def __init__(self, taste=''):
        self.taste = taste

    def print_taste(self):
        return f"У вас обычная газировка" if not self.taste else f'К вас газировка со вкусом {self.taste.lower()}'


strawberry = Soda('Клубника')
strawberry.print_taste()
