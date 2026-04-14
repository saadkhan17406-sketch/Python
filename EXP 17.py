#https://github.com/saadkhan17406-sketch/Python
print ("UIN : 251A053")
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        self.items.append({"product": product, "quantity": quantity})
        print(f"Added {quantity} x {product.name} to cart.")

    def calculate_total(self):
        total = sum(item["product"].price * item["quantity"] for item in self.items)
        return total

p1 = Product("Laptop", 50000)
p2 = Product("Mouse", 1000)

cart = ShoppingCart()
cart.add_item(p1, 1)
cart.add_item(p2, 2)

total = cart.calculate_total()
print(f"Total Bill: Rs. {total:.2f}")