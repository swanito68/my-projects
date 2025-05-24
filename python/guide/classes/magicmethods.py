# Magic methods =   Dunder methods (double underscore) __init__, __str__, __eq__
#                   they are automatically called by many of Python's built+in operations.
#                   They allow developers to define or customize the behaviour of objects

# Let's make a class of books:
class Book:
    # Let's make a constructor magic method:
    def __init__(self, title, author, pgNumber):
        self.title = title
        self.author = author
        self.pgNumber = pgNumber

    # If you try to print any oobject, it will return a memory address.
    # So let's make a __str__ magic method:
    def __str__(self):  # It takes one parameter of "self"
        return f"{self.title} by {self.author}"
        # It will modify how printing the object reacts

    # If we try to compare two objects, it will still return False even if all of the values are the some
    # So let's make an __eq__ magic method:
    def __eq__(self, other):  # other means the other books
        return self.title == other.title and self.author == other.author

    # If we try to compare two objects with lesser than or greater than, it will return an error
    # So let's make an __lt__ and __gt__ magic method:
    def __lt__(self, other):
        return self.pgNumber < other.pgNumber

    def __gt__(self, other):
        return self.pgNumber > other.pgNumber

    # What if we want to add the page numbers?
    # So let's make an __add__ magic method:
    def __add__(self, other):
        return self.pgNumber + other.pgNumber

    # What if we wanted to search for a keyword?
    # SO let's make a __contains__ magic method:
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author

    # What if we wanted to index it?
    # So let's make a __getitem__ magic method:
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "pages" or key == "pgNumber":
            return f"{self.pgNumber} pages"
        else:
            return f"Key {key} was not found"


# Let's make some objects:
book1 = Book("The Hobbit", "J.R.R Tolkien", 310)
book2 = Book("the Lion, the Witch and the Wardrobe", "C.S Lewis", 172)
book3 = Book("harry Potter and The Philosopher's Stone", "J.K Rowling", 223)
book4 = Book("The Hobbit", "not jrr tolken", 310 + (310 / 4) ** -1)

print(book1)
print(book1 == book4)
print(book3 > book1)
print(book2 < book4)
print(book1 + book2)
print("Lion" in book2)
print("Lion" in book4)
print(book2["title"], book1["pages"], book4["author"])
