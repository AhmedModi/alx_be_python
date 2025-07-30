import sys
from bank_account import BankAccount

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
        account.deposit(amount)  # Already prints
    elif command == "withdraw" and amount is not None:
        account.withdraw(amount)  # Already prints
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command")
