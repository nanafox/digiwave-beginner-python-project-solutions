#!/usr/bin/env python3

"""Simple Banking App.

The simple banking app simulates basic banking operations such as displaying balance,
depositing money, and withdrawing money. It allows users to interactively manage their account balance.
"""


def display_balance(balance: float) -> None:
    print(f"Your account balance: ${balance}")


def deposit(balance: float) -> float:
    amount = float(input("Enter amount to deposit: "))
    if amount > 0:
        balance += amount
        print(f"Deposited ${amount}. New balance: ${balance}")
    else:
        print("Deposit amount must be positive.")
    return balance


def withdraw(balance: float) -> float:
    amount = float(input("Enter amount to withdraw: "))
    if amount > 0:
        if amount <= balance:
            balance -= amount
            print(f"Withdrew ${amount}. New balance: ${balance}")
        else:
            print("Insufficient funds.")
    else:
        print("Withdrawal amount must be positive.")
    return balance


def main():
    balance = 0
    while True:
        print("\nSimple Banking App")
        print("1. Display Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Quit")
        choice = input("Choose an option (1-4): ")
        print()

        if choice == "1":
            display_balance(balance)
        elif choice == "2":
            balance = deposit(balance)
        elif choice == "3":
            balance = withdraw(balance)
        elif choice == "4":
            print("Thank you for using the Simple Banking App. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
