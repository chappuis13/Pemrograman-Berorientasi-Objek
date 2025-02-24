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
    Book("Harry Potter", "J.K. Rowling", "978-3-16-148410-0"),
    Book("The Hobbit", "J.R.R. Tolkien", "978-3-16-148410-1"),
    Book("The Lord of the Rings", "J.R.R. Tolkien", "978-3-16-148410-2"),
    Book("The Chronicles of Narnia", "C.S. Lewis", "978-3-16-148410-3"),
    Book("The Hunger Games", "Suzanne Collins", "978-3-16-148410-4"),
    Book("Twilight", "Stephenie Meyer", "978-3-16-148410-5"),
    Book("The Da Vinci Code", "Dan Brown", "978-3-16-148410-6"),    
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