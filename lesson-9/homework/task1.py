class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) >= 3:
            raise MemberLimitExceededException(f"{self.name} cannot borrow more than 3 books.")
        if book.is_borrowed:
            raise BookAlreadyBorrowedException(f"The book '{book.title}' is already borrowed.")
        self.borrowed_books.append(book)
        book.is_borrowed = True

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.is_borrowed = False

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, title, author):
        self.books.append(Book(title, author))

    def add_member(self, name):
        self.members.append(Member(name))

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        raise BookNotFoundException(f"Book '{title}' not found.")

    def find_member(self, name):
        for member in self.members:
            if member.name == name:
                return member
        return None

library = Library()
library.add_book("1984", "George Orwell")
library.add_book("Python 101", "John Doe")
library.add_member("Alice")

try:
    book = library.find_book("1984")
    member = library.find_member("Alice")
    member.borrow_book(book)
    print("Book borrowed successfully.")
    member.borrow_book(book)
except Exception as e:
    print(e)

try:
    book = library.find_book("Nonexistent Book")
except Exception as e:
    print(e)

try:
    book1 = library.find_book("Python 101")
    member.borrow_book(book1)
    book2 = Book("Extra Book", "Author")
    book3 = Book("Another Book", "Author")
    member.borrow_book(book2)
    member.borrow_book(book3)
except Exception as e:
    print(e)