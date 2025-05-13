
# ==========================================
# Custom Exceptions for Order Processing
# ==========================================
class OrderError(Exception):
    """Base class for order processing errors."""
    pass

class OutOfStockError(OrderError):
    """Raised when a product is out of stock."""
    def __init__(self, product_id, requested, available):
        message = (f"Product {product_id} is out of stock: "
                   f"requested {requested}, available {available}.")
        super().__init__(message)

class PaymentDeclinedError(OrderError):
    """Raised when a payment is declined by the payment gateway."""
    def __init__(self, reason):
        message = f"Payment declined: {reason}"
        super().__init__(message)

class InvalidShippingAddressError(OrderError):
    """Raised when the shipping address is invalid."""
    def __init__(self, address):
        message = f"Invalid shipping address: '{address}'."
        super().__init__(message)


# ==========================================
# System Components
# ==========================================
class Inventory:
    def __init__(self, stock):
        self.stock = stock

    def reserve(self, product_id, quantity):
        available = self.stock.get(product_id, 0)
        if quantity > available:
            raise OutOfStockError(product_id, quantity, available)
        self.stock[product_id] -= quantity
        print(f"[Inventory] Reserved {quantity} unit(s) of {product_id}.")

class PaymentProcessor:
    def __init__(self, user_balance):
        self.user_balance = user_balance

    def charge(self, amount):
        if amount > self.user_balance:
            raise PaymentDeclinedError("Insufficient funds")
        self.user_balance -= amount
        print(f"[Payment] Charged ${amount:.2f}. Remaining balance: ${self.user_balance:.2f}.")

class ShippingService:
    def validate_address(self, address):
        parts = address.strip().split()
        if len(parts) < 2 or not parts[-1].isdigit():
            raise InvalidShippingAddressError(address)
        print(f"[Shipping] Address '{address}' is valid.")


# ==========================================
# Order Processing Function
# ==========================================
def process_order(product_id, qty, price_per_unit, shipping_address,
                  inventory, payment_processor, shipping_service):
    try:
        inventory.reserve(product_id, qty)
        shipping_service.validate_address(shipping_address)
        total = qty * price_per_unit
        payment_processor.charge(total)

    except OutOfStockError as e:
        print(f"Order failed: {e}")
    except InvalidShippingAddressError as e:
        print(f"Order failed: {e}")
    except PaymentDeclinedError as e:
        print(f"Order failed: {e}")
    else:
        print("Order succeeded!")
    finally:
        print("Order process complete.\n")


# ==========================================
# Additional Program 1: User Authentication System
# ==========================================
class AuthError(Exception):
    pass

class UserNotFoundError(AuthError):
    def __init__(self, username):
        super().__init__(f"User '{username}' not found.")

class InvalidPasswordError(AuthError):
    def __init__(self):
        super().__init__("Invalid password provided.")

class AccountLockedError(AuthError):
    def __init__(self):
        super().__init__("Account is locked due to multiple failed login attempts.")

class AuthSystem:
    def __init__(self):
        self.users = {
            "alice": {"password": "secret123", "locked": False, "attempts": 0}
        }

    def login(self, username, password):
        if username not in self.users:
            raise UserNotFoundError(username)

        user = self.users[username]
        if user["locked"]:
            raise AccountLockedError()

        if password != user["password"]:
            user["attempts"] += 1
            if user["attempts"] >= 3:
                user["locked"] = True
            raise InvalidPasswordError()

        user["attempts"] = 0
        print(f"[Auth] Welcome, {username}!")


# ==========================================
# Additional Program 2: File Backup Manager
# ==========================================
class BackupError(Exception):
    pass

class FileNotFoundBackupError(BackupError):
    def __init__(self, file_path):
        super().__init__(f"File not found: {file_path}")

class InsufficientStorageError(BackupError):
    def __init__(self, needed, available):
        super().__init__(f"Not enough storage: needed {needed}MB, available {available}MB.")

class BackupManager:
    def __init__(self, storage_mb):
        self.storage_mb = storage_mb

    def backup(self, file_path, file_size_mb):
        if file_path != "important.docx":
            raise FileNotFoundBackupError(file_path)
        if file_size_mb > self.storage_mb:
            raise InsufficientStorageError(file_size_mb, self.storage_mb)

        self.storage_mb -= file_size_mb
        print(f"[Backup] '{file_path}' backed up. Remaining storage: {self.storage_mb}MB")


# ==========================================
# Additional Program 3: Bank ATM Simulator
# ==========================================
class ATMError(Exception):
    pass

class InsufficientFundsError(ATMError):
    def __init__(self, balance, requested):
        super().__init__(f"Requested ${requested}, but balance is only ${balance}.")

class DailyLimitExceededError(ATMError):
    def __init__(self, requested, limit):
        super().__init__(f"Daily limit exceeded: requested ${requested}, limit is ${limit}.")

class ATM:
    def __init__(self, balance, daily_limit):
        self.balance = balance
        self.daily_limit = daily_limit

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        if amount > self.daily_limit:
            raise DailyLimitExceededError(amount, self.daily_limit)

        self.balance -= amount
        print(f"[ATM] Dispensed ${amount}. Remaining balance: ${self.balance}")


# ==========================================
# Example Executions
# ==========================================
if __name__ == "__main__":
    # Order Processing
    inv = Inventory(stock={"SKU123": 5, "SKU999": 0})
    pay = PaymentProcessor(user_balance=100.00)
    ship = ShippingService()

    process_order("SKU123", 2, 20.00, "10 Merdeka St 10110", inv, pay, ship)
    process_order("SKU999", 1, 50.00, "10 Merdeka St 10110", inv, pay, ship)
    process_order("SKU123", 1, 20.00, "Boulevard Raya", inv, pay, ship)
    process_order("SKU123", 3, 30.00, "10 Merdeka St 10110", inv, pay, ship)

    # Auth System
    auth = AuthSystem()
    try:
        auth.login("bob", "wrongpass")
    except AuthError as e:
        print(f"Login failed: {e}")

    # Backup Manager
    backup = BackupManager(storage_mb=100)
    try:
        backup.backup("unknown.docx", 20)
    except BackupError as e:
        print(f"Backup failed: {e}")

    # ATM Simulator
    atm = ATM(balance=500, daily_limit=300)
    try:
        atm.withdraw(350)
    except ATMError as e:
        print(f"Withdrawal failed: {e}")
