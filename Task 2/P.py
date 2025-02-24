class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        print(f"{self.owner} deposited {amount}. New Balance: ${self.balance}")
        
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"{self.owner} withdrew {amount}. New Balance: ${self.balance}")
            
    def check_balance(self):
        print(f"Balance: ${self.balance}")
        
    def show_info(self):
        print(f"Owner: {self.owner}")
        print(f"Balance: ${self.balance}")
    
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
        owner = input("Enter account owner name: ")
        balance = float(input("Enter initial balance: "))
        account = BankAccount(owner, balance)
        accounts.append(account)
        print("Account created successfully.")
    
    elif menu == "2":
        for i, account in enumerate(accounts):
            print(f"{i+1}. {account.owner}")
    
    elif menu == "3":
        account_index = int(input("Enter account number: ")) - 1
        amount = float(input("Enter deposit amount: "))
        accounts[account_index].deposit(amount)
    
    elif menu == "4":
        account_index = int(input("Enter account number: ")) - 1
        amount = float(input("Enter withdrawal amount: "))
        accounts[account_index].withdraw(amount)
    
    elif menu == "5":
        account_index = int(input("Enter account number: ")) - 1
        accounts[account_index].check_balance()
    
    elif menu == "6":
        print("Exiting...")
        break