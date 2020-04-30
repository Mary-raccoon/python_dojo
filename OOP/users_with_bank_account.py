class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    def make_deposit(self, amount):
        self.account.balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account.balance -= amount
        return self

    def display_user_balance(self):
        print(f"{self.name}'s ballance: ${self.account.balance}")
    
    def transfer_money(self, other_user, amount):
        self.account.balance -= amount
        other_user.account.balance += amount
        return self

class BankAccount:
    def __init__(self, int_rate=0.02, balance=0): 
        self.int_rate = int_rate
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        return self
        
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return self
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
            return self
        
    def display_account_info(self):
        print(f"Balance: ${self.balance}")

    def yield_interest(self):
        if self.balance >= 0:
            self.balance += self.balance * self.int_rate
            return self


mary = User("Mary", "mary@yahoo.com")
alex = User("Alex", "alex@yahoo.com")


mary.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(500).display_user_balance()

alex.make_deposit(400).make_deposit(400).make_withdrawal(500).make_withdrawal(50).transfer_money(mary, 100).display_user_balance()

mary.display_user_balance()

mary.deposit()

