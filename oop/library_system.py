class Book:
    def __str__(self, title, author):
        self.title = title
        self.author = author

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            if isinstance(self, EBook):
                print(f"EBook: {book.title} by {book.author}, File Size: {book.file_size}MB")
            elif isinstance(self, PrintBook):
                print(f"Print Book: {book.title} by {book.author}, Page Count: {book.page_count}")
        else:
            print(f"Book: {book.title} by {book.author}")
            
