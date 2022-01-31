class Product:
    def __init__(self, name, price, discountPercent):
        self.name = name
        self.price = price
        self.discountPercent = discountPercent
        self.discountedAmount = self.price * self.discountPercent

    def getDiscountAmount(self):
        return self.price - self.getDiscountPrice()

    def getDiscountPrice(self):
        return (self.price * self.discountPercent) / 100


product1 = Product(name="Stanley Hammer", price=12.99, discountPercent=62)
prodcut2 = Product(name='nails', price=5.06, discountPercent=0)

print(product1.getDiscountPrice())
print(product1.getDiscountAmount())
