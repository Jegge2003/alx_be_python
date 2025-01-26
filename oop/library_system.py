class Book:
    #Initializing class attributes
    def __init__(self, title:str, author:str):
        self.title = title
        self.author = author

    def __str__(self):
        return f'Book: {self.title} by {self.author}'

class EBook(Book):
    #Initilizing class attributes
    def __init__(self, title:str, author:str, file_size:int):
        #Calling parent class's __init__ to initiliaze parent attributes
        super().__init__(title, author)
        #Adding additional attributes
        self.file_size = file_size

    def __str__(self):
        return f'EBook: {self.title} by {self.author}, File Size: {self.file_size}KB'

class PrintBook(Book):
    #Initializing class attributes
    def __init__(self, title:str, author:str, page_count:int):
        #Calling parent class's __init__ to initialize parent attributes
        super().__init__(title, author)
        #Adding additional attributes
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

class Library:
    #Initializing class attributes
    def __init__(self):
        self.books = []

    def add_book(self, book):
        """Addds a Book, EBook, or PrintBook instance to the library"""
        self.books.append(book)

    def list_books(self):
        """Prints details of each book in library"""
        if not self.books:
            print('No books in library')
        else:
            for book in self.books:
                print(book)
        
