import store

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
