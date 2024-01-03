from django.db import models

# Define the Book model using Django's models
class Book(models.Model):
    # Fields for the Book model: title, author, and ISBN
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    ISBN = models.CharField(max_length=100)

    # Constructor for the Book class
    # def __init__(self,title,author,ISBN):
    #     self.title = title
    #     self.author = author
    #     self.ISBN = ISBN

    # Method to display information about the book
    def display(self):
        print(f"Title:{self.title} \t Author:{self.author} \t ISBN: {self.ISBN}")
    
    # Metadata for the Book model with the database table name as book
    class Meta:
        db_table = "book"

# Define the Ebook model as a subclass of Book
class Ebook(Book):

    # Constructor for the Ebook class, inheriting from Book and adding fileformat
    def __init__(self,title,author,ISBN,fileformat):
        super().__init__(title,author,ISBN)
        self.fileformat = fileformat

    # Method to display information about the ebook, calling the superclass display method
    def display(self):
        super().display()
        print(f"\tFileformat:{self.fileformat}")

# Define the Library class
class Library:

     # Constructor for the Library class, initializing an empty list for books
    def __init__(self):
        self.books = []

     # Method to add a book to the library
    def add_book(self, book):
        self.books.append(book)
    
    # Method to display information about all books in the library
    def display_all_books(self):
        for book in self.books:
            book.display()
            print("---------------")
    
    # Method to search for a book by title in the library
    def search_book_by_title(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None


# Creating instances of Book, EBook, and Library classes
book1 = Book("Python Basics", "John Doe", "978-1-123456-78-9")
ebook1 = Ebook("Flask Web Development", "Jane Smith", "978-1-987654-32-1", "PDF")
library = Library()

# Adding books to the library
library.add_book(book1)
library.add_book(ebook1)

# Displaying all books in the library
library.display_all_books()

# Searching for a book by title
searched_book = library.search_book_by_title("Python Basics")
if searched_book:
    print("Book Found:")
    searched_book.display()
else:
    print("Book not found.")