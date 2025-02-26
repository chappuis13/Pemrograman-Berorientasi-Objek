class BankAccount:
    def __init__(self, account_holder, balance, pin):
        self.ownerName = account_holder
        self._balance = balance
        self.__pin = pin
        self.accountNumber = len(accounts) + 1
        
    def set_balance(self, amount):
        self._balance += amount
        print(f"\n{self.ownerName} deposited {amount}. New Balance: ${self._balance}")

    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
            print(f"\n{self.ownerName} withdrew {amount}. New Balance: ${self._balance}")
        else:
            print("Insufficient Balance")

    def get_balance(self):
        print(f"\nAccount Balance for {self.ownerName}: ${self._balance}")
    
    def verify_pin(self, pin):
        if not pin.isdigit() or len(pin) != 4:
            print("Invalid PIN. Please enter a 4-digit number.")
            return False
        return self.__pin == pin
        
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
            ownerName = input("\nEnter account owner name: ")
            balance = float(input("Enter initial balance: "))
            pin = input("Enter 4-digit pin: ")
            if not pin.isdigit() or len(pin) != 4:
                print("\nInvalid PIN. Please enter a 4-digit number.")
                continue
            account = BankAccount(ownerName, balance, pin)
            accounts.append(account)
            print(f"\nAccount created successfully. Account Number: {account.accountNumber}")
        except ValueError:
            print("\nInvalid input. Please enter a valid number for the balance.")
    
    elif menu == "2":
        if accounts:
            print("\nAccounts:")
            for account in accounts:
                print(f"{account.accountNumber} | Owner: {account.ownerName}")
        else:
            print("\nNo accounts found.")
    
    elif menu == "3":
        try:
            account_number = int(input("\nEnter account number: "))
            account = next((acc for acc in accounts if acc.accountNumber == account_number), None)
            if account:
                pin = input("Enter 4-digit pin: ")
                if account.verify_pin(pin):
                    amount = float(input("Enter deposit amount: "))
                    account.deposit(amount)
                else:
                    print("\nInvalid PIN. Access denied.")
            else:
                print("\nAccount not found.")
        except ValueError:
            print("\nInvalid input. Please enter a valid number for the account number and deposit amount.")
    
    elif menu == "4":
        try:
            account_number = int(input("\nEnter account number: "))
            account = next((acc for acc in accounts if acc.accountNumber == account_number), None)
            if account:
                pin = input("Enter 4-digit pin: ")
                if account.verify_pin(pin):
                    amount = float(input("Enter withdrawal amount: "))
                    account.withdraw(amount)
                else:
                    print("\nInvalid PIN. Access denied.")
            else:
                print("\nAccount not found.")
        except ValueError:
            print("\nInvalid input. Please enter a valid number for the account number and withdrawal amount.")
    
    elif menu == "5":
        try:
            account_number = int(input("\nEnter account number: "))
            account = next((acc for acc in accounts if acc.accountNumber == account_number), None)
            if account:
                pin = input("Enter 4-digit pin: ")
                if account.verify_pin(pin):
                    account.get_balance()
                else:
                    print("\nInvalid PIN. Access denied.")
            else:
                print("\nAccount not found.")
        except ValueError:
            print("\nInvalid input. Please enter a valid number for the account number.")
    
    elif menu == "6":
        print("\nGoodbye!")
        break
    
    else:
        print("\nInvalid option. Please try again.")