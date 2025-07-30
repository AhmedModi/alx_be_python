import sys
from bank_account import BankAccount

if __name__ == "__main__":
    account = BankAccount(250)

    # ✅ Change 1: Handle the case where no arguments are passed
    if len(sys.argv) == 1:
        print(account.display_balance())
        sys.exit(0)

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
    
    # ✅ Change 2: Broaden acceptable display command names
    elif command in ["display", "display_balance"]:
        print(account.display_balance())
    else:
        print("Invalid command")
