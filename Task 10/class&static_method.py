class BankAccount:
    # Class variables
    bank_name = "Global Banking Corp."
    interest_rate = 0.02  # 2% annual interest rate
    total_accounts = 0
    
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance
        self.account_number = f"ACC-{BankAccount.total_accounts + 1000}"
        self.is_active = True
        BankAccount.total_accounts += 1
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        return "Invalid deposit amount."
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        return "Insufficient funds or invalid amount."
    
    @classmethod
    def create_joint_account(cls, account_holder1, account_holder2, initial_deposit=0):
        joint_name = f"{account_holder1} & {account_holder2}"
        print(f"Creating joint account for {joint_name}")
        return cls(joint_name, initial_deposit)
    
    @classmethod
    def update_interest_rate(cls, new_rate):
        if 0 <= new_rate <= 0.1:  # Ensure rate is reasonable (0-10%)
            cls.interest_rate = new_rate
            return f"Interest rate updated to {new_rate:.1%}"
        return "Invalid interest rate"
    
    @staticmethod
    def validate_account_number(account_number):
        if not isinstance(account_number, str):
            return False
        
        # Check format (ACC-followed by 4 digits)
        if not (account_number.startswith("ACC-") and 
                len(account_number) == 8 and 
                account_number[4:].isdigit()):
            return False
            
        return True
    
    @staticmethod
    def calculate_loan_payment(principal, annual_rate, years):
        # Convert annual rate to monthly rate and years to months
        monthly_rate = annual_rate / 12
        months = years * 12
        
        # Calculate monthly payment using loan formula
        if monthly_rate == 0:
            return principal / months
        
        monthly_payment = principal * (monthly_rate * (1 + monthly_rate)**months) / ((1 + monthly_rate)**months - 1)
        return monthly_payment


# Demonstration
if __name__ == "__main__":
    # Create a regular account
    alice_account = BankAccount("Alice Smith", 1000)
    print(f"Created account for {alice_account.account_holder}")
    print(f"Account number: {alice_account.account_number}")
    print(f"Initial balance: ${alice_account.balance}")
    
    # Use instance methods
    print(alice_account.deposit(500))
    print(alice_account.withdraw(200))
    
    # Use class method to create a joint account
    joint_account = BankAccount.create_joint_account("Bob Johnson", "Carol Johnson", 2000)
    print(f"Joint account holders: {joint_account.account_holder}")
    print(f"Joint account number: {joint_account.account_number}")
    print(f"Joint account balance: ${joint_account.balance}")
    
    # Use class method to update a class variable
    print(f"Current interest rate: {BankAccount.interest_rate:.1%}")
    print(BankAccount.update_interest_rate(0.03))
    print(f"New interest rate for all accounts: {alice_account.interest_rate:.1%}")
    
    # Use static methods - note they don't change any instance or class state
    account_to_validate = "ACC-1234"
    print(f"Is {account_to_validate} valid? {BankAccount.validate_account_number(account_to_validate)}")
    
    # Calculate loan payment using static method
    loan_amount = 10000
    loan_rate = 0.05  # 5%
    loan_years = 5
    monthly_payment = BankAccount.calculate_loan_payment(loan_amount, loan_rate, loan_years)
    print(f"Monthly payment for ${loan_amount} loan at {loan_rate:.1%} for {loan_years} years: ${monthly_payment:.2f}")
    
    # Show total accounts created
    print(f"Total accounts created: {BankAccount.total_accounts}")