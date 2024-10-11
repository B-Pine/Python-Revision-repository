import string
import random


class Book:
    """The book object will be created every time new book is brought into the
    library"""

    def __init__(self, name: str, year: int, category: str, author: str =
    'Author'):
        self._id = book_id_generator()
        self._name = name
        self._category = category
        self._author = author
        self._year = year
        self._availability = True

    @property
    # getters code for the `_name` attribute
    def name(self):
        return self._name

    @property
    def availability(self):
        return self._availability

    @availability.setter
    def availability(self, status):
        self._availability = status


class Library:
    """The library class will store all the books available.
    Attributes:
       _name: The name of the library. If not specified will default to 
            'Library'.
    Methods:
        add_book: To add book to the library.
        borrow_book: To borrow book from the library.
    """""

    def __init__(self, name: str = 'Library'):
        self._name = name
        self._available_books = []
        self._borrowed_books = []

    @property
    def library_name(self):
        return self._name

    @property
    def available_book(self):
        return self._available_books

    @property
    def borrowed_books(self):
        return self._borrowed_books

    def add_book(self, book: Book):
        """Method will be used to add book to list of available books in
        library."""
        if book.availability:
            self._available_books.append(book)
            print("Book added to library successfully.")

    def borrow_book(self, book: Book):
        """Method  will handle the borrowing of book.
        If the book os borrowed it will be removed from the available books
        and appended to the borrowed books."""
        if book.availability:
            self._borrowed_books.append(book)
            # self._available_books.remove(book)
            print(f"You've just borrowed {book.name}")
            book.availability = False
        else:
            print(f"{book.name} not available for borrow")


def book_id_generator():
    """The function is used to generate book id."""
    book_id = []
    stack = list(string.ascii_lowercase + string.digits)
    random.shuffle(stack)

    for item in range(16):
        book_id.append(random.choice(stack))
        random.shuffle(stack)

    return "".join(book_id)


def view_available_books(libray: Library):
    """The function will retrieve the available books and """
    count = 1
    for book in libray.available_book:
        print(f"\t\t{count}. {book.name}")
        count += 1


def book_availability_checker(book_name: str, library: Library):
    """Method will traverse through either list of books"""
    for obj in library.available_book:
        if obj.name.casefold() == book_name.casefold():
            return obj
    for obj in library.borrowed_books:
        if obj.name.casefold() == book_name.casefold():
            return None

    return "\t\tBook not in library (store) yet."


def initials(library: Library):  # TODO This method should be deleted
    book1 = Book('Oxford Dictionary', 2012, "Dictionary", 'Oxford')
    book2 = Book('Gatanya I', 2024, "Poetry", 'Jr.')
    library.add_book(book1)
    library.add_book(book2)


def initialise():
    """The method to initialise the system."""

    print("===Welcome on Library management System LMS===")

    input("Press Enter to proceed in Hewitt Library")
    library = Library('Hewitt')
    initials(library)

    menu = ["View available books", "Borrow book", "Purchase book"]

    while True:
        print()
        # printing menu on the screen
        print(f"\tChoose from the the menu::{library.library_name}")
        print("-" * 40)
        for option, menu_item in enumerate(menu):
            print(f"\t{option + 1}. {menu_item}")
        print("\t0. Quit")  # printing quit option on the screen

        choice = int(input(">> "))
        if choice == 0:
            break
        if choice == 1:
            view_available_books(library)
        elif choice == 2:
            borrow_book_name = input("Enter name of the book: ")
            borrowed = book_availability_checker(borrow_book_name, library)
            if borrowed is None:
                # the msg is passed in 'Library' class.
                pass
            elif type(borrowed) is str:
                print(borrowed)
            else:
                library.borrow_book(borrowed)

        elif choice == 3:
            print("Feature coming soon!")
        else:
            print("Wrong choice!")


if __name__ == "__main__":
    initialise()
