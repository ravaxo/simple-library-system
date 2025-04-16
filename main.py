'''This is the main module where it calls the classes by creating objects, 
This is where the logic comes together'''
from book import Book
from user import User
from library import Library

# Create library
library = Library()

# Create books with unique book_id
book_1 = Book("Python 101", "John Doe", "01")
book_2 = Book("Automate Boring Stuff with Python", "Al Sweigart", "02")
book_3 = Book("Elliott Wave Principle: Key to Market Behavior", "Robert Prechter,", "03")

# Create users with unique user_id
a001 = User("migara")
a002 = User("ravindi")

# Add books to the library
library.add_book(book_1)
library.add_book(book_2)
library.add_book(book_3)

# Add users to the library
library.add_user(a001)
library.add_user(a002)

# Test borrowing and returning
library.borrow_book(a001, book_1)
print(book_1.get_status())
library.return_book(a001, book_2)
print(book_1.get_status())
print(a001.get_borrowed_books())
print(library.available_books())
print(library.get_name(a001))
