from product import Product
from productmanager import ProductManager

product1 = Product("Laptop", 1000, 5)
product2 = Product("Phone", 500, 10)
product3 = Product("Headphones", 100, 20)

manager = ProductManager()

manager.add_product(product1)
manager.add_product(product2)
manager.add_product(product3)

manager.display_products()

print("\nTotal Inventory Value: " +str(manager.calculate_total_value()))
