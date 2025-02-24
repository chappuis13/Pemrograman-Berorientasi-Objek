class BankAccount:
    def __init__(self, ownerName, balance=0):
        self.ownerName = ownerName
        self.balance = balance
        self.accountNumber = len(accounts) + 1
        
    def deposit(self, amount):
        self.balance += amount
        print(f"{self.ownerName} deposited {amount}. New Balance: ${self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"{self.ownerName} withdrew {amount}. New Balance: ${self.balance}")
        else:
            print("Insufficient Balance")

    def check_balance(self):
        print(f"Account Balance for {self.ownerName}: ${self.balance}")
        
accounts = []

while True:
    print("\nBank Account Menu:")
    print("1. Create Account")
    print("2. List Accounts")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Check Balance")
    print("6. Exit")
    
    menu = input("Select an option: ")
    
    if menu == "1":
        try:
            ownerName = input("Enter account owner name: ")
            balance = float(input("Enter initial balance: "))
            account = BankAccount(ownerName, balance)
            accounts.append(account)
            print(f"Account created successfully. Account Number: {account.accountNumber}")
        except ValueError:
            print("Invalid input. Please enter a valid number for the balance.")
    
    elif menu == "2":
        if accounts:
            for account in accounts:
                print(f"Account Number: {account.accountNumber}, Owner: {account.ownerName}")
        else:
            print("No accounts found.")
    
    elif menu == "3":
        try:
            account_number = int(input("Enter account number: "))
            account = next((acc for acc in accounts if acc.accountNumber == account_number), None)
            if account:
                amount = float(input("Enter deposit amount: "))
                account.deposit(amount)
            else:
                print("Account not found.")
        except ValueError:
            print("Invalid input. Please enter a valid number for the account number and deposit amount.")
    
    elif menu == "4":
        try:
            account_number = int(input("Enter account number: "))
            account = next((acc for acc in accounts if acc.accountNumber == account_number), None)
            if account:
                amount = float(input("Enter withdrawal amount: "))
                account.withdraw(amount)
            else:
                print("Account not found.")
        except ValueError:
            print("Invalid input. Please enter a valid number for the account number and withdrawal amount.")
    
    elif menu == "5":
        try:
            account_number = int(input("Enter account number: "))
            account = next((acc for acc in accounts if acc.accountNumber == account_number), None)
            if account:
                account.check_balance()
            else:
                print("Account not found.")
        except ValueError:
            print("Invalid input. Please enter a valid number for the account number.")
    
    elif menu == "6":
        break
    
    else:
        print("Invalid option. Please try again.")