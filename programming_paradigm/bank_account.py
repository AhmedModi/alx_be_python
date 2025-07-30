class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = float(initial_balance)

   def deposit(self, amount):
    self.balance += amount
    print(f"Deposited: ${amount:.1f}") 

   def withdraw(self, amount):
    if amount > self.balance:
        print("Insufficient funds.")
    else:
        self.balance -= amount
        print(f'Withdrew: ${amount:.1f}')

    def display_balance(self):
        print(f"Current Balance: ${self.balance:.2f}")
