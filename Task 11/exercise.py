import json
import os

file_path = 'books.json'
if os.path.exists(file_path):
    with open(file_path, 'r') as file:
        books = json.load(file)
else:
    books = []

def save_books():
    with open(file_path, 'w') as file:
        json.dump(books, file)

def add_book():
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    year = input("Enter publication year: ")
    genre = input("Enter book genre: ")
    borrowed = input("Is the book borrowed? (yes/no): ").lower() == 'yes'
    book = {
        'title': title,
        'author': author,
        'year': year,
        'genre': genre,
        'borrowed': borrowed
    }
    
    books.append(book)
    save_books()
    print(f"Book '{title}' added successfully!")
    list_books()
    
def list_books():
    for index, book in enumerate(books):
        print("-" * 20)
        print(f"Number: {index + 1}")
        print(f"Title: {book['title']}")
        print(f"Author: {book['author']}")
        print(f"Year: {book['year']}")
        print(f"Genre: {book['genre']}")
        print(f"Borrowed: {'Yes' if book['borrowed'] else 'No'}")
    print("-" * 20)
        
def edit_book():
    list_books()
    no_book = input("Choose book number to edit: ")
    new_book = books[int(no_book) - 1]
    
    print("Current details:")
    print(f"1. Title: {new_book['title']}")
    print(f"2. Author: {new_book['author']}")
    print(f"3. Year: {new_book['year']}")
    print(f"4. Genre: {new_book['genre']}")
    print(f"5. Borrowed: {'Yes' if new_book['borrowed'] else 'No'}")
    
    update_book = input("Choose which detail to update (1-5): ")
    if update_book == '1':
        new_book['title'] = input("Enter new title: ")
    elif update_book == '2':
        new_book['author'] = input("Enter new author: ")
    elif update_book == '3':
        new_book['year'] = input("Enter new publication year: ")
    elif update_book == '4':
        new_book['genre'] = input("Enter new genre: ")
    elif update_book == '5':
        new_book['borrowed'] = input("Is the book borrowed? (yes/no): ").lower() == 'yes'
    else:
        print("Invalid choice, no changes made.")
    
    books[int(no_book) - 1] = new_book
    save_books()
    print("Book updated successfully!")
    
def delete_book():
    list_books()
    no_book = input("Choose book number to delete: ")
    books.pop(int(no_book) - 1)
    save_books()
    print("Book deleted successfully!")
    

while True:
    print("Choose an option:")
    print("1. Add Book")
    print("2. List Books")
    print("3. Edit Book")
    print("4. Delete Book")
    print("5. Exit")
    
    menu = input("Enter your choice: ")
    if menu == '1':
        add_book()
    elif menu == '2':
        list_books()
    elif menu == '3':
        edit_book()
    elif menu == '4':
        delete_book()
    elif menu == '5':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice, please try again.")