'''This module handles the functions of a simple library'''
class Library:
    '''The Library class keeps tracks of user and books,
    and update the relevant details'''

    def __init__(self):
        self.__user = []
        self.__book = []

    def get_name(self, user):
        '''returns the name'''
        return user.get_name()

    def add_user(self, user):
        '''add users to the library'''
        self.__user.append(user)

    def add_book(self, book):
        '''add books to the library using book object'''
        self.__book.append(book)

    def borrow_book(self, user, book):
        '''librarian can update if a user borrowed a book'''
        user.set_borrowed_books(book)

    def return_book(self, user, book):
        '''librarian can update if a user borrowed a book'''
        user.set_returned_books(book)

    def available_books(self):
        '''returns a list of available books'''
        return [item.get_title() for item in self.__book if item.get_status() == "Available"]
