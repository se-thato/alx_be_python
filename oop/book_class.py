class Book:
    def __init__(self,title, author, year) -> None:
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        print(f"Deleting {self.title}")

    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"
    
    def __repr__(self):
        return f"Book ('{self.title}', '{self.author}', {self.year})"
    

if __name__ == "__main__":
    book = Book('2002', 'Thato', '1964')
    print(str(book))
    print(repr(book))
    