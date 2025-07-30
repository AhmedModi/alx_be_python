import sys
from bank_account import BankAccount

if __name__ == "__main__":
    account = BankAccount(250)

    if len(sys.argv) == 1:
        account.display_balance()
        sys.exit()

    command_input = sys.argv[1]

    if ':' in command_input:
        command, value = command_input.split(':')
        amount = float(value)
    else:
        command = command_input
        amount = None

    if command == "deposit" and amount is not None:
        account.deposit(amount)
    elif command == "withdraw" and amount is not None:
        account.withdraw(amount)
    elif command in ["display", "display_balance"]:
        account.display_balance()
    else:
        print("Invalid command")
