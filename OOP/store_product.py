class Store:
    def __init__(self, name, list_of_prod=[]):
        self.name = name
        self.list_of_prod = []


    def add_product(self, new_product):
        self.list_of_prod.append({"id": new_product.id,
                                  "name": new_product.name, 
                                  "price": new_product.price,
                                  "category": new_product.category
                                  })
        return self

    def print_info(self):
        print(f"Name: {self.name}, List: {self.list_of_prod}")
        return self
    
    def sell_product(self, id):
        for i in self.list_of_prod:
            if i["id"] == id:
                self.list_of_prod.remove(i)
                print("Removed Product:", i)       
        return self
    
    def inflation(self, percent_increase):
        for i in self.list_of_prod:
            i['price'] += i['price'] * percent_increase
        return self

    def set_clearance(self, category, percent_discount):
        for i in self.list_of_prod:
            if i['category'] == category:
                i['price'] -= i['price'] * percent_discount
        return self

class Product:
    def __init__(self, id, name, price, category):
        self.id = id
        self.name = name
        self.price = price
        self.category = category
    
    def update_price(self, percent_change=0.02, is_increased=True):
        if is_increased == True:
            self.price += self.price * percent_change
            return self
        else:
            self.price -= self.price * percent_change 
            return self  
    def print_info(self):
        print(f"Id: {self.id}, Name: {self.name}, category: {self.category}, price: {self.price}")

store1 = Store("Walmart")
store2 = Store("Costco")

prod1 = Product(101, "potato", 5.00, "food")
prod2 = Product(102,"banana", 5.00, "food")
prod3 = Product(103, "dress", 100, "clothes")

# prod1.update_price(0.1, False).print_info()
# prod2.update_price().print_info()

store1.add_product(prod1).add_product(prod2).sell_product(102).inflation(0.07).print_info()
store2.add_product(prod1).add_product(prod2).add_product(prod3).set_clearance("clothes", 0.1).print_info()
