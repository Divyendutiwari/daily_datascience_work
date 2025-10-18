class bank:
    def __init__(self,name,account_number,balance):
        self.name=name
        self.account_number=account_number
        self.balance=balance
    def display_balance(self):
        return f"Account Holder: {self.name}, Account Number: {self.account_number}, Balance: ${self.balance}"
    def add_value(self,amount):
        self.balance += amount
        return f"New Balance after adding ${amount}: ${self.balance}"
    def withdraw_value(self,amount):
        return f"New Balance after withdrawing ${amount}: ${self.balance} - amount"
my_account=bank("Alice", "123456789", 1000)
print(my_account.add_value(500))
print(my_account.withdraw_value(200))
print(my_account.display_balance())