class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = float(initial_balance)

    def deposit(self, amount):
        self.balance += float(amount)
        print(f"Deposited: ${float(amount)}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= float(amount)
            print(f"Withdrew: ${float(amount)}")

    def display_balance(self):
        print(f"Current Balance: ${self.balance:.2f}")
