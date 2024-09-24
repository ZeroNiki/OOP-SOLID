"""
Creating classes to manage the library
"""


class Book:
    def __init__(self, title, author, year, isbn):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year}) - ISBN: {self.isbn}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, isbn):
        self.books = [book for book in self.books if book.isbn != isbn]

    def find_book(self, query):
        return [
            str(book) for book in self.books
            if query.lower() in book.title.lower()
            or query.lower() in book.author.lower()
        ]

    def list_books(self):
        return [str(book) for book in self.books]
