class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    
    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"{self.name}'s ballance: ${self.account_balance}")
    
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self

mary = User("Mary", "mary@yahoo.com")
alex = User("Alex", "alex@yahoo.com")


mary.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(500).display_user_balance()

alex.make_deposit(400).make_deposit(400).make_withdrawal(500).make_withdrawal(50).transfer_money(mary, 100).display_user_balance()

mary.display_user_balance()

