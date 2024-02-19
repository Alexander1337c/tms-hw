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

    @property
    def product_id(self):
        return self.__id_x

    def __str__(self):
        return f'{self.__id_x, self.__name, self.__name_store, self.__cost_in_byn}'


class Stock:
    def __init__(self, products: list = None):
        self.__products = []
        for product in products:
            self.add_product(product)

    def __getitem__(self, value):
        for item in self.__products:
            if isinstance(value, str):
                if item.name.lower() == value.lower():
                    return item
            elif isinstance(value, int):
                if value > len(self.__products):
                    raise ValueError('Product not found')
                elif item.product_id == value:
                    return item
        raise ValueError(f'Product {value} not found')

    def __add__(self, other):
        if not isinstance(other, (Stock, Product)):
            raise TypeError('Onli string object of Stock')
        return sum(item.price for item in self.__products) + sum(item.price for item in other.__products)

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError('Item must be object of Product')
        self.__products.append(product)

    def sort_product_by_price(self):
        self.__products.sort(key=lambda e: e.price)
        return self.__products

    def sort_product_by_name(self):
        self.__products.sort(key=lambda e: e.name_product)
        return self.__products

    def sort_product_by_store(self):
        self.__products.sort(key=lambda e: e.name_store)
        return self.__products


a = Stock([
    Product("iphone XR", 'i-store', 1200),
    Product("iphone 12", 'i-store', 1000),
    Product("iphone 8", '21vek', 790),
    Product("Samsung s10", 'amd.by', 1800),
    Product("Indesit", 'diy', 920),
])
b = Stock([Product("iphone 4", 'i-store', 700)])
a.add_product(Product("iphone 5s", 'i-store', 1150))
try:
    print('--------------------------')
    # a.sort_product_by_store()
    c = a + b
    print(c)
    print(a[3] + a['iphone 12'])
    print(a['iphone 12'])

    # print(b.id_x)
except Exception as e:
    print(e)
