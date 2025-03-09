class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds.")

class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        if self.balance >= amount:
            if amount <= 500:
                self.balance -= amount
                print(f"Withdrew ${amount}. New balance: ${self.balance}")
            else:
                print("Cannot withdraw more than $500 at a time.")
        else:
            print("Insufficient funds.")
            
class PremiumSavingsAccount(SavingsAccount):
    def withdraw(self, amount):
        if self.balance >= amount:
            if amount <= 1000:
                self.balance -= amount
                print(f"Withdrew ${amount}. New balance: ${self.balance}")
            else:
                print("Cannot withdraw more than $1000 at a time.")
        else:
            print("Insufficient funds.")
            
accounts = [
    SavingsAccount(1, 1000),
    PremiumSavingsAccount(2, 2000)
]

while True:
    print("\nBank Account Menu:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    
    menu = input("Select an option: ")
    
    if menu == "1":
        account_number = int(input("Enter account number: "))
        amount = float(input("Enter amount to deposit: "))
        for account in accounts:
            if account.account_number == account_number:
                account.deposit(amount)
                break
        else:
            print("Account not found.")
    
    elif menu == "2":
        account_number = int(input("Enter account number: "))
        amount = float(input("Enter amount to withdraw: "))
        for account in accounts:
            if account.account_number == account_number:
                account.withdraw(amount)
                break
        else:
            print("Account not found.")
    
    elif menu == "3":
        account_number = int(input("Enter account number: "))
        for account in accounts:
            if account.account_number == account_number:
                print(f"Account balance: ${account.balance}")
                break
        else:
            print("Account not found.")
    
    elif menu == "4":
        break
    
    else:
        print("Invalid option. Please try again.")