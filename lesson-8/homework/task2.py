import json
import random

class Account:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def to_dict(self):
        return {
            "account_number": self.account_number,
            "name": self.name,
            "balance": self.balance
        }


class Bank:
    def __init__(self):
        self.accounts = {}
        self.load_from_file()

    def create_account(self, name, initial_deposit):
        acc_num = str(random.randint(10000, 99999))
        while acc_num in self.accounts:
            acc_num = str(random.randint(10000, 99999))
        account = Account(acc_num, name, initial_deposit)
        self.accounts[acc_num] = account
        self.save_to_file()
        print(f"Account created! Number: {acc_num}")

    def view_account(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            print(account.to_dict())
        else:
            print("Account not found.")

    def deposit(self, account_number, amount):
        if amount <= 0:
            print("Invalid amount.")
            return
        account = self.accounts.get(account_number)
        if account:
            account.balance += amount
            self.save_to_file()
            print(f"Deposited {amount}. New balance: {account.balance}")
        else:
            print("Account not found.")

    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if not account:
            print("Account not found.")
            return
        if amount > account.balance:
            print("Insufficient funds.")
            return
        account.balance -= amount
        self.save_to_file()
        print(f"Withdrew {amount}. New balance: {account.balance}")

    def save_to_file(self):
        with open("accounts.txt", "w") as f:
            json.dump({acc: self.accounts[acc].to_dict() for acc in self.accounts}, f)

    def load_from_file(self):
        try:
            with open("accounts.txt", "r") as f:
                data = json.load(f)
                for acc_num, info in data.items():
                    self.accounts[acc_num] = Account(**info)
        except FileNotFoundError:
            self.accounts = {}