class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def display_info(self):
        print("Product: " + self.name + ", Price: " + str(self.price) + ", Quantity: " + str(self.quantity))
    
    def upradte_quantity(self, new_quantity):
        self.quantity = new_quantity
    