class Soda:
    def __init__(self, taste=''):
        self.taste = taste

    def print_taste(self):
        print("У вас обычная газировка") if not self.taste else print(f'К вас газировка со вкусом {self.taste.lower()}')


strawberry = Soda('Клубника')
strawberry.print_taste()