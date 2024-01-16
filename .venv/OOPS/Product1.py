class Product1:
    quantity=400
    def __init__(self,name,price):
        self.name=name
        self.price=price

    def summer_discount(self,discount_percent):
        self.price=self.price-self.price*discount_percent/100

p1=Product1("Tshirt",10)
print(p1.name)
print(p1.price)
p1.summer_discount(10)
print(p1.price)

p2=Product1("Phone",400)
p2.summer_discount(50)
print(p2.price)