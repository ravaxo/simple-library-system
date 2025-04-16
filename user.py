'''This module keeps track of users and books borrowed'''
class User:
    '''User class, keeps track of the name and borrowed book'''

    def __init__(self, name):
        self.__name = name.title()
        self.__borrowed_books = []

    def get_name(self):
        '''returns the name of the user'''
        return self.__name

    def set_borrowed_books(self, book):
        '''checks the user already has 3 books, if yes returns,
        set the names of the borrowed books by a user and updates its Borrowed'''

        if len(self.__borrowed_books) >= 3:
            print(f"{self.__name}, you've reached the borrowing limit of 3 books!")
            return

        if book.get_status() == 'Available':
            book.set_status('Borrowed')
            self.__borrowed_books.append(book)

        elif book in self.__borrowed_books:
            print(f"You already have that book {self.__name}")

        else:
            print(f"Sorry, the book you're searching is unavailable {self.__name}")

    def get_borrowed_books(self):
        '''returns the borrowed books by a specific user'''
        return [book.get_title() for book in self.__borrowed_books]

    def set_returned_books(self, book):
        '''set the names of the returned books by a user and updates its Available'''
        if book in self.__borrowed_books:
            self.__borrowed_books.remove(book)
            book.set_status('Available')
        else:
            print("Wrong book!!!")
