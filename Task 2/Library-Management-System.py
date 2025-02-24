class Book:
    def __init__(self, title, author, ISBN, available=True):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.available = available

    def borrowbook(self):
        if self.available:
            self.available = False
            print(f"{self.title} by {self.author} has been borrowed.")
        else:
            print(f"{self.title} by {self.author} is not available.")

    def returnbook(self):
        if not self.available:
            self.available = True
            print(f"{self.title} by {self.author} has been returned.")
        else:
            print(f"{self.title} by {self.author} is already available.")
            
books = [
    Book("1984", "George Orwell", "978-0-452-28423-4"),
    Book("To Kill a Mockingbird", "Harper Lee", "978-0-06-112008-4"),
    Book("Pride and Prejudice", "Jane Austen", "978-0-14-143951-8"),
    Book("The Catcher in the Rye", "J.D. Salinger", "978-0-316-76948-0"),
    Book("Moby-Dick", "Herman Melville", "978-0-14-243724-7"),
    Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0-7432-7356-5"),
    Book("Brave New World", "Aldous Huxley", "978-0-06-085052-4"),
]

borrowed_books = []

while True:
    print("\nLibrary Menu:")
    print("1. Borrow Book")
    print("2. Return Book")
    print("3. Exit")
    
    menu = input("Select an option: ")
    
    if menu == "1":
        try:
            for i, book in enumerate(books):
                print(f"{i+1}. {book.title} by {book.author}")
            book_index = int(input("Enter book number: ")) - 1
            if 0 <= book_index < len(books):
                if books[book_index] in borrowed_books:
                    print("Book is already borrowed.")
                    continue
                books[book_index].borrowbook()
                borrowed_books.append(books[book_index])
            else:
                print("Invalid book number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    elif menu == "2":
        try:
            if borrowed_books:
                for i, book in enumerate(borrowed_books):
                    print(f"{i+1}. {book.title} by {book.author}")
                book_index = int(input("Enter book number: ")) - 1
                if 0 <= book_index < len(borrowed_books):
                    borrowed_books[book_index].returnbook()
                    borrowed_books.remove(borrowed_books[book_index])
                else:
                    print("Invalid book number.")
            else:
                print("No borrowed books found.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    elif menu == "3":
        break
    
    else:
        print("Invalid option. Please select a valid option.")
