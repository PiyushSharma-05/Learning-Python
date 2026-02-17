class Product:
    count = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.count += 1

    def get_info(self): #instance method
        print(f"og price of {self.name} is {self.price}")

    @classmethod
    def get_count(cls):
        print(f"total products in store is: {cls.count}")
    
    @staticmethod
    def calc_discount(price, discount):
        final_price = price - (price*discount/100)
        print(f"discounted price is: {final_price}")

p1 = Product("laptop", 50_000)
p2 = Product("phone", 15_000)
p3 = Product("washing machine", 30_000)
p4 = Product("earphone", 1_000)

p1.get_info()
p2.get_info()
p3.get_info()
p4.get_info()

p1.calc_discount(p1.price, 10)
p2.calc_discount(p2.price, 10)
p3.calc_discount(p3.price, 10)
p4.calc_discount(p4.price, 18)

Product.get_count()