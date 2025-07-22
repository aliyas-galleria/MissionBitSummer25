from io import BufferedRandom


class Smartphone:
    def __init__(self, brand, model, storage): # Class constructor
        self.brand = brand # Initializes brand
        self.model = model # Initializes model
        self.storage = storage # Initializes storage

    def display_info(self): # Method to display smartphone info
        print(f"Smartphone: {self.brand} {self.model}, Storage: {self.storage}GB")

# Creating two objects
my_phone = Smartphone("Apple", "iPhone 13", 128)
your_phone = Smartphone("Samsung", "Galaxy S22", 256)
their_phone = Smartphone("Google", "Pixel 9", 128)

# Using a method to display info about the phones
my_phone.display_info()  # Outputs -> Smartphone: Apple iPhone 13, Storage: 128GB
your_phone.display_info() # Outputs -> Smartphone: Samsung Galaxy S22, Storage: 256GB
their_phone.display_info()

from pydoc import describe


class Book:

    def __init__(self, title="Animal Farm", author="George Orwell", year=1945):
        self.title = title
        self.author = author
        self.year = year

    def describe(self):
        print(f"Book: {self.title}, By: {self.author}, Published: {self.year}")

    def is_classic(self):
        if self.year < 1970:
            return True
        return False

    def __str__(self):
        return str(self.__dict__)

my_book = Book("Harry Potter", "J.K. Rowling", 1997)
your_book = Book("Pride and Prejudice", "Jane Austen", 1813)
their_book = Book("To Kill a Mockingbird", "Harper Lee", 1960)
book = Book()

print(book)

my_book.describe()
your_book.describe()
their_book.describe()

print(my_book.is_classic())
print(your_book.is_classic())
print(their_book.is_classic())

print(my_book)

def describe():
    book1 = Book("Harry Potter", "J.K. Rowling", 1997)

describe()
