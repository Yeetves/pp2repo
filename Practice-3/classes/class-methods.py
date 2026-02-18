class Calc:
    def add(self, a, b):
        return a+b
    def multiply(self, a, b):
        return a*b
    
c = Calc()
print(c.add(7, 3))
print(c.multiply(4, 5))


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_info(self):
        return f"{self.name} is {self.age} years old"
    
p1 = Person("Adik", 34)
print(p1.get_info())

# or __str__ method can be used here

class Cattie:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Cattie {self.name} is {self.age} years old"
    
cat1 = Cattie("Munya", 3)
print(cat1)


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
    def add_book(self, book):
        self.books.append(book)
        print(f"Added {book}")
    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
        print(f"Removed {book}")
    
    def show_books(self):
        print(f"Our library '{self.name}':")
        for book in self.books:
            print(f"-{book}")

my_library = Library("Modern literature")
my_library.add_book("Demian")
my_library.add_book("The Steppe wolf")
my_library.add_book("Frankenshtein")
my_library.show_books()