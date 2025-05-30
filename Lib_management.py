class Book:
    """
    A mutable class to represent a book in the library.
    """

    def __init__(self, title: str, author: str, genre: str, available: bool =True):
        """
        Initialize a Book object.

        Parameters:
        title (str): The title of the book.
        author (str): The name of the book's writer.
        genre (str): Genre of the book.
        available (bool): Whether the book is available (default is True).
        """
        self.title = title
        self.author = author
        self.genre = genre
        self.available = available

    def __str__(self):
        """
        Return a string with the book representation.

        Returns:
        str: Details of the book and its availability status.
        """
        status = "Available" if self.available else "Borrowed"
        return f"'{self.title}' by {self.author} - Genre: {self.genre} [{status}]"


class BookNotFoundException(Exception):
    """
    Raised when a book is not found in the library.
    """
    pass


class BookAlreadyBorrowedException(Exception):
    """
    Raised when a book is already borrowed.
    """
    pass


class Library:
    """
    A class to manage a collection of books in a library.
    """

    def __init__(self):
        """
        Initialize the library with an empty book list.
        """
        self.books = []

    def add_book(self, book):
        """
        Add a new book to the library.

        Parameters:
        book (Book): The book to be added.
        """
        self.books.append(book)

    def search_books(self, keyword):
        """
        Search for books by title, author, or genre.

        Parameters:
        keyword (str): The keyword to search for.

        Returns:
        list of Book: List of books that match the keyword.
        """
        keyword = keyword.lower()
        found = [book for book in self.books if
                 keyword in book.title.lower() or
                 keyword in book.author.lower() or
                 keyword in book.genre.lower()]
        return found

    def borrow_book(self, title):
        """
        Borrow a book from the library by title.

        Parameters:
        title (str): The title of the book to borrow.

        Returns:
        str: Confirmation message.

        Raises:
        BookAlreadyBorrowedException: If the book is already borrowed.
        BookNotFoundException: If the book does not exist in the library.
        """
        for book in self.books:
            if book.title.lower() == title.lower():
                if not book.available:
                    raise BookAlreadyBorrowedException(f"'{title}' is already borrowed.")
                book.available = False
                return f"You've successfully borrowed '{title}'"
        raise BookNotFoundException(f"Book titled '{title}' not found.")

    def return_book(self, title):
        """
        Return a book to the library by title.

        Parameters:
        title (str): The title of the book to return.

        Returns:
        str: Confirmation message.

        Raises:
        BookNotFoundException: If the book does not exist in the library.
        """
        for book in self.books:
            if book.title.lower() == title.lower():
                book.available = True
                return f"'{title}' has been returned."
        raise BookNotFoundException(f"Book titled '{title}' not found.")



if __name__ == "__main__":
    library = Library()

    # Adding some books
    library.add_book(Book("The Maze Runner", "James Dashner", "Classic"))
    library.add_book(Book("Pride and Prejudice", "Jane Auston", "Classic"))
    library.add_book(Book("The God of small things", "Arundati Roy", "Indian fiction"))
    library.add_book(Book("Data Science 101", "Jane Doe", "Education"))

    # Search books
    print("\n Search for 'classic':")
    for book in library.search_books("classic"):
        print(book)

    # Borrow a book
    try:
        print("\n Borrowing 'Pride and Prejudice':")
        print(library.borrow_book("Pride and Prejudice"))
    except Exception as e:
        print("Error:", e)

    # Try borrowing again
    try:
        print("\n Borrowing 'Pride and Prejudice:")
        print(library.borrow_book("Pride and Prejudice"))
    except Exception as e:
        print("Error:", e)

    # Return the book
    try:
        print("\n Returning 'Pride and Prejudice':")
        print(library.return_book("Pride and Prejudice"))
    except Exception as e:
        print("Error:", e)

    # Try to borrow a non-existing book
    try:
        print("\n Borrowing 'Nonexistent Book':")
        print(library.borrow_book("Nonexistent Book"))
    except Exception as e:
        print("Error:", e)
