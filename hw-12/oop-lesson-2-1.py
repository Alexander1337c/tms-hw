class Product:
    id_x = 1

    def __init__(self, name_product, name_store, cost_in_byn):
        self.__id_x = Product.id_x
        self.__name = name_product
        self.__name_store = name_store
        self.__cost_in_byn = cost_in_byn
        Product.id_x += 1

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def name_store(self):
        return self.__name
    @name_store.setter
    def name_store(self, name_store):
        self.__name_store = name_store

    @property
    def price(self):
        return self.__cost_in_byn

    @price.setter
    def price(self, price):
        self.__cost_in_byn = price

    def __str__(self):
        return f'{self.__name, self.__name_store, self.__cost_in_byn}'


class Stock:
    def __init__(self, products: list = None, name='', price=''):
        self.name = name
        self.price = price
        self.__products = []
        for product in products:
            if not isinstance(product, Product):
                raise TypeError('Товары могут быть только объектом класса Product')
            self.add_product(product)

    def add_method(self, name=''):
        self.name = name
        for items in self.__products:
            if items['name_product'].lower() == name.lower():
                self.price = items['price']
            else:
                raise ValueError('Такого товара нет')
        return self.price

    def add_product(self, product):
        id_x, name, name_store, price = product.__dict__.keys()
        obj = {'id': product.__dict__[id_x],
               'name_product': product.__dict__[name],
               'name_store': product.__dict__[name_store],
               'price': product.__dict__[price]
               }
        self.__products.append(obj)

    def print_products(self):
        print(self.__products)

    def print_product_id(self, id_prod):
        result = list(filter(lambda item: int(item['id']) == id_prod, self.__products))
        return result

    def print_product_name(self, name):
        items = list(filter(lambda item: item['name_product'].lower() == name.lower(), self.__products))
        return items

    def __add__(self, other):
        if not isinstance(other, Stock):
            raise TypeError('Только строка объекта класса Stock')
        print(self, other)
        return self.price + other.price

    def sort_product_price(self):
        self.__products.sort(key=lambda e: e['price'])
        return self.__products

    def sort_product_name(self):
        self.__products.sort(key=lambda e: e['name_product'])
        return self.__products

    def sort_product_store(self):
        self.__products.sort(key=lambda e: e['name_store'])
        return self.__products


a = Stock([
    Product("iphone XR", 'i-store', 1200),
    Product("iphone X", 'i-store', 1000),
    Product("iphone 8", '21vek', 790),
    Product("Samsung s10", 'amd.by', 1800),
    Product("Indesit", 'diy', 920),
])
b = Product("iphone 4", 'i-store', 700)
a.add_product(Product("iphone 5s", 'i-store', 1150))
a.add_product(b)
a.print_products()
print(a.print_product_id(3))
print(a.print_product_name('iphone xr'))
print(a.sort_product_store())

c1 = a.add_method('iphone xr')
c2 = a.add_method('iphone x')
c3 = c1 + c2
print(c3)
