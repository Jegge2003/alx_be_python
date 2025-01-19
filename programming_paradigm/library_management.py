class Book:
    #Represents a book in the library

    def __init__(self, title, author):
        #Initialize a Book instance with a title, author, and availability status

        self.title = title
        self.author = author
        self._is_checked_out = False #Private attribute to track availability

    def check_out(self):
        #Mark the book as checked out
        self._is_checked_out = True

    def return_book(self):
        #Mark the book as available
        self._is_checked_out = False

    def is_available(self):
        #Check if the book is available for checkout
        return not self._is_checked_out

class Library:
    #Represents a library containing a collection of books

    def __init__(self):
        #Initialize a Library instance with an empty collection of books
        self._books = [] #Private list to store Book instances

    def add_book(self, book):
        #Add a book to the library's collection.
        self._books.append(book)
        print(f'Book "{book.title}" by {book.author} added to the library.')

    def check_out_book(self, title):
        #Check out a book by its title.
        for book in self._books:
            if book.title == title:
                if book.is_available():
                    book.check_out()
                    print(f'Book "{title}" has been checked out.')
                    return True
                else:
                    print(f'Book "{title}" is already checked out.')
                    return False
        print(f'Book "{title}" not found in the library.')
        return False

    def return_book(self, title):
        #Return a book by its title
        for book in self._books:
            if book.title == title:
                if not book.is_available():
                    book.return_book()
                    print(f'Book "{title}" has been returned.')
                    return True
                else:
                    print(f'Book "{title}" was not checked out.')
                    return False
        print(f'Book "{title}" not found in the library.')
        return False

    def list_available_books(self):
        #List all books that are currently available for checkout.
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            print('Available books:')
            for book in available_books:
                print(f'- "{book.title}" by {book.author}')
        else:
            print('No books are currently available.')

