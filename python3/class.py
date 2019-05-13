# ref : https://wikidocs.net/89

# Class Paper
class Paper:
    page = 100

    def __init__(self, page):
        self.page = page

    def __repr__(self):
        return self.page

    def getPage(self):
        return self.page

# Class Book -> Class Paper
class Book(Paper):
    title = ""
    price = 0
    author = ""

    # Constructor
    def __init__(self, title, price, author):
        self.setData(title, price, author)
        print('Create Book : ', title)

    # Destructor
    def __del__(self):
        print('Delete Book :', self.title)

    # Print this book element
    # print book
    def __repr__(self):
        return "title : " + self.title

    # Overload +
    def __add__(self, other):
        return self.price + other.price

    # Overload -
    def __sub__(self, other):
        return self.price - other.price

    # Overload >, <, == / no longer use
    def __cmp__(self, other):
        if self.price < other.price:
            return -1
        elif self.price == other.price:
            return 0
        else:
            return 1

    # Overload <, >
    def __lt__(self, other):
        if self.price < other.price:
            return False
        else:
            return True

    # Overload ==
    def __eq__(self, other):
        if self.price == other.price:
            return True
        else:
            return False

    def setData(self, title, price, author):
        self.title = title
        self.price = price
        self.author = author



book1 = Book("Les Thanatonautes", 10000, "Bernard Werber")
book2 = Book("TEST1", 5000, "DUMMY1")
book3 = Book("TEST2", 5000, "DUMMY2")

print("book1", book1)
print("Overload : book1 + book2", book1 + book2)
print("Overload : book1 < book2", book1 < book2)
print("Overload : book1 > book2", book1 > book2)
print("Overload : book1 == book2", book1 == book2)
print("Overload : book2 == book3", book2 == book3)
print("Paper : book1.getPage()", book1.getPage())



