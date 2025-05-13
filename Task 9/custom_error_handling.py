# Custom Exceptions
class LibraryError(Exception):
    """Base class for library system errors."""
    pass

class BookNotAvailableError(LibraryError):
    """Raised when a book is not available for borrowing."""
    def __init__(self, book_id, requested, available):
        message = (f"Book {book_id} is not available: "
                   f"requested {requested}, available {available}.")
        super().__init__(message)

class MembershipExpiredError(LibraryError):
    """Raised when a user tries to borrow a book with an expired membership."""
    def __init__(self):
        message = "Membership expired. Please renew to borrow books."
        super().__init__(message)

class BorrowLimitExceededError(LibraryError):
    """Raised when a user tries to borrow more books than allowed."""
    def __init__(self, limit):
        message = f"Borrow limit exceeded. Max allowed: {limit} books."
        super().__init__(message)


# System Components
class LibraryCatalog:
    def __init__(self, stock):
        # stock: dict mapping book_id to quantity available
        self.stock = stock

    def reserve(self, book_id, quantity):
        available = self.stock.get(book_id, 0)
        if quantity > available:
            raise BookNotAvailableError(book_id, quantity, available)
        self.stock[book_id] -= quantity
        print(f"[Catalog] Reserved {quantity} copy/copies of {book_id}.")

class MembershipManager:
    def __init__(self, is_active, borrowed_books, limit):
        self.is_active = is_active
        self.borrowed_books = borrowed_books
        self.limit = limit

    def authorize(self, quantity):
        if not self.is_active:
            raise MembershipExpiredError()
        if self.borrowed_books + quantity > self.limit:
            raise BorrowLimitExceededError(self.limit)
        self.borrowed_books += quantity
        print(f"[Membership] Authorized borrowing of {quantity} book(s). Now borrowed: {self.borrowed_books}.")

class LibraryRulesService:
    def check_eligibility(self, member_id):
        # Placeholder logic
        print(f"[Rules] Member {member_id} is eligible to borrow books.")


# Book Borrowing Function
def borrow_book(book_id, qty, member_id,
                catalog, membership_manager, rules_service):
    try:
        # 1. Check book availability
        catalog.reserve(book_id, qty)

        # 2. Check member eligibility
        rules_service.check_eligibility(member_id)

        # 3. Authorize borrowing
        membership_manager.authorize(qty)

    except BookNotAvailableError as e:
        print(f"Borrowing failed: {e}")
    except MembershipExpiredError as e:
        print(f"Borrowing failed: {e}")
    except BorrowLimitExceededError as e:
        print(f"Borrowing failed: {e}")
    else:
        print("Book borrowing succeeded! Enjoy reading.")
    finally:
        print("Borrowing process complete.\n")


# Example Execution
if __name__ == "__main__":
    catalog = LibraryCatalog(stock={"BOOK123": 3, "BOOK999": 0})
    member = MembershipManager(is_active=True, borrowed_books=1, limit=5)
    rules = LibraryRulesService()

    # 1. Successful borrow
    borrow_book(
        book_id="BOOK123",
        qty=2,
        member_id="MEM001",
        catalog=catalog,
        membership_manager=member,
        rules_service=rules
    )

    # 2. Book not available
    borrow_book(
        book_id="BOOK999",
        qty=1,
        member_id="MEM001",
        catalog=catalog,
        membership_manager=member,
        rules_service=rules
    )

    # 3. Membership expired
    member_expired = MembershipManager(is_active=False, borrowed_books=0, limit=5)
    borrow_book(
        book_id="BOOK123",
        qty=1,
        member_id="MEM002",
        catalog=catalog,
        membership_manager=member_expired,
        rules_service=rules
    )

    # 4. Borrow limit exceeded
    member_limit = MembershipManager(is_active=True, borrowed_books=4, limit=5)
    borrow_book(
        book_id="BOOK123",
        qty=2,
        member_id="MEM003",
        catalog=catalog,
        membership_manager=member_limit,
        rules_service=rules
    )
