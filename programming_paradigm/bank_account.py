class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = float(initial_balance)

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            return False
        else:
            self.balance -= amount
            return True
     def display_balance(self):
        return f"Current Balance: ${self.balance:.2f}"
