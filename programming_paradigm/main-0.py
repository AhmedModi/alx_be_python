import sys
from bank_account import BankAccount
from robust_division_calculator import safe_divide

account = BankAccount(250)
account.display_balance()  # Should print the balance, not return it

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    numerator = sys.argv[1]
    denominator = sys.argv[2]

    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    account = BankAccount(100)

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        sys.exit(1)

    command_input = sys.argv[1]
    if ':' in command_input:
        command, value = command_input.split(':')
        amount = float(value)
    else:
        command = command_input
        amount = None

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount:.1f}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f'Withdrew: ${amount:.1f}')
        else:
            print("Insufficient funds.")
    elif command == "display":
        print(account.display_balance())
    else:
        print("Invalid command")
