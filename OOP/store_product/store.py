


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