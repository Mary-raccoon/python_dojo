import store 
import product

store1 = Store("Walmart")
store2 = Store("Costco")

prod1 = Product(101, "potato", 5.00, "food")
prod2 = Product(102,"banana", 5.00, "food")
prod3 = Product(103, "dress", 100, "clothes")

# prod1.update_price(0.1, False).print_info()
# prod2.update_price().print_info()

store1.add_product(prod1).add_product(prod2).sell_product(102).inflation(0.07).print_info()
store2.add_product(prod1).add_product(prod2).add_product(prod3).set_clearance("clothes", 0.1).print_info()
