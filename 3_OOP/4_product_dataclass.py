from dataclasses import dataclass # Step 1: import dataclass


@dataclass # step 2: add dataclass decorator
class Product:
    # step 3: create attributes inside the class directly
    name: str
    price: int
    discountPercent: int

    def getDiscountAmount(self):
        return self.price - self.getDiscountPrice()

    def getDiscountPrice(self):
        return (self.price * self.discountPercent) / 100


product1 = Product(name="Stanley Hammer", price=12.99, discountPercent=62)
prodcut2 = Product(name='nails', price=5.06, discountPercent=0)

print(product1.getDiscountPrice())
print(product1.getDiscountAmount())
