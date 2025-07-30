class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = float(initial_balance)

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
            return False
        else:
            self.balance -= amount
            print(f'Withdrew: ${amount}')
            return True

    def display_balance(self):
        print(f"Current Balance: ${self.balance:.2f}")
