'''This module keep track of the book availability and there information'''

class Book:
    '''A blueprint to create book objects'''

    def __init__(self, title, author, isbn):
        self.__title = title.title()
        self.__author = author
        self.__isbn = isbn
        self.__status = 'Available'

    def get_title(self):
        '''returns the title of the book'''
        return self.__title

    def get_author(self):
        '''Return the author of the book.'''
        return self.__author

    def get_status(self):
        '''Return the availability status of the book.'''
        return self.__status

    def get_isbn(self):
        '''returns the isbn'''
        return self.__isbn

    def get_details(self):
        '''Take the details of the book title, author and availability,
        return those details'''
        return f"{self.__title} by {self.__author} - {self.__status}"

    def set_status(self, status):
        '''Changes the availability status only to Available or Borrowed and returns the bool'''
        if status.title() in ['Available', 'Borrowed']:
            self.__status = status.title()
            return True

        print("Invalid status!")
        return False
