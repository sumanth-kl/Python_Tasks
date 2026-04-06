"""16. Library Management System (Constructor & Inheritance)
A library stores information about books and digital books. Create a base class Book
with a constructor to initialize book details. Create a derived class EBook that adds file
size information."""


class Book:
    def __init__(self,title):
        self.title=title

class EBook(Book):
    def __init__(self,title,size):
        Book.__init__(self,title)
        self.size=size

    def display(self):
        print("Book:",self.title)
        print("File Size:",self.size,"MB")

my_book = EBook("Python", 2)
my_book.display()
