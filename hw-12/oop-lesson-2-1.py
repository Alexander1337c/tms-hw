class Product:
    __name_product = ''
    __name_store = ''
    __cost_in_byn = 0


class Stock:
    __products = [{'id': '1', "name_product": "iphone XR", 'name_store': 'i-store', 'price': 1200},
                  {'id': '2', "name_product": "iphone X", 'name_store': 'i-store', 'price': 1000},
                  {'id': '3', "name_product": "iphone 8", 'name_store': '21vek', 'price': 790},
                  {'id': '4', "name_product": "Samsung s10", 'name_store': 'amd.by', 'price': 1800},
                  {'id': '5', "name_product": "Indesit", 'name_store': 'diy', 'price': 920}
                  ]

    def __init__(self, name=''):
        self.name = name
        for items in self.__products:
            if items['name_product'].lower() == name.lower():
                self.price = items['price']

    @classmethod
    def print_product_id(cls, id_prod):
        result = list(filter(lambda item: int(item['id']) == id_prod, cls.__products))
        return result

    @classmethod
    def print_product_name(cls, name):
        items = list(filter(lambda item: item['name_product'].lower() == name.lower(), cls.__products))
        return items

    def __add__(self, other):
        if not isinstance(other, Stock):
            raise TypeError('Только строка')
        return self.price + other.price

    @classmethod
    def sort_product_store(cls):
        res = sorted(cls.__products, key=lambda item: item['name_store'])
        return res

    @classmethod
    def sort_product_name(cls):
        res = sorted(cls.__products, key=lambda item: item['name_product'])
        return res

    @classmethod
    def sort_product_price(cls):
        res = sorted(cls.__products, key=lambda item: item['price'])
        return res


Stock.print_products()
print(Stock.print_product_id(3))
print(Stock.print_product_name('iphone XR'))
c1 = Stock('iphone XR')
c2 = Stock('iphone X')
c3 = Stock('indesit')
print(c1 + c2)
print(Stock.sort_product_store())
