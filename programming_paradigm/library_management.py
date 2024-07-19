class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        False

    def return_books(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True 
        return False
    
    def is_available(self):
        return not self._is_checked_out

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_available():
                book.check_out()
                return f"Book '{title}' is not available."
            
    def return_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return f"Book '{title}' has been returned."
            return f"Book '{title}' was not checked out."
        
    def list_available_book(self):
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            return "No books are available."
        return [f"Title: {book.title}, Author: {book.author}" for book in available_books]


book1 = Book("The selfish gene", "Richard Dawkins" )
book2 = Book("The magic stick", "John Mark")

library = Library()

library.add_book(book1)
library.add_book(book2)

#list of available books
print("Available book:", library.list_available_book())

#checkout book
print(library.check_out_book("2002 war"))

#available books after check out 
print("Available books:", library.list_available_book())

#return the book
print(library.return_book('2002 war'))

#list of books after a book is returned 
print("Available books:", library.list_available_book())
