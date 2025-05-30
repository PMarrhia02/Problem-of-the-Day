from typing import List, Optional


class Book:
    """A class to represent a book in the library system."""

    def __init__(self, title: str, author: str, genre: str, available: bool = True) -> None:
        """Initialize a Book instance.

        Args:
            title: Title of the book.
            author: Author of the book.
            genre: Genre of the book.
            available: Availability status (default: True).
        """
        self.title = title
        self.author = author
        self.genre = genre
        self.available = available

    def __str__(self) -> str:
        """Return string representation of the book.

        Returns:
            Formatted string with book details.
        """
        status = "Available" if self.available else "Borrowed"
        return f"{self.title} by {self.author} | {self.genre} | {status}"


class BookNotFoundException(Exception):
    """Exception raised when a book is not found."""
    pass


class BookAlreadyBorrowedException(Exception):
    """Exception raised when a book is already borrowed."""
    pass


class Library:
    """A class to manage library book operations."""

    def __init__(self, books: Optional[List[Book]] = None) -> None:
        """Initialize the library with optional list of books.

        Args:
            books: Optional initial list of books.
        """
        self.books = books or []

    def search_books(self, field: str, keyword: str) -> List[Book]:
        """Search books by field (title/author/genre).

        Args:
            field: Attribute to search ('title', 'author', or 'genre').
            keyword: Search term.

        Returns:
            List of matching Book objects.
        """
        keyword = keyword.lower()
        return [
            book for book in self.books
            if keyword in getattr(book, field).lower()
        ]

    def borrow_book(self, title: str) -> str:
        """Borrow a book by title.

        Args:
            title: Title of book to borrow.

        Returns:
            Confirmation message.

        Raises:
            BookNotFoundException: If book doesn't exist.
            BookAlreadyBorrowedException: If book is already borrowed.
        """
        book = self._find_book(title)
        if not book.available:
            raise BookAlreadyBorrowedException(f"'{title}' is already borrowed.")
        book.available = False
        return f"You borrowed '{title}'."

    def return_book(self, title: str) -> str:
        """Return a borrowed book.

        Args:
            title: Title of book to return.

        Returns:
            Confirmation message.

        Raises:
            BookNotFoundException: If book doesn't exist.
        """
        book = self._find_book(title)
        if book.available:
            return f"'{title}' was not borrowed."
        book.available = True
        return f"You returned '{title}'."

    def _find_book(self, title: str) -> Book:
        """Find a book by title (case-insensitive).

        Args:
            title: Title to search for.

        Returns:
            The matching Book object.

        Raises:
            BookNotFoundException: If no match found.
        """
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        raise BookNotFoundException(f"'{title}' not found.")


def display_menu() -> None:
    """Display the main menu options."""
    print("\n1. Search Book\n2. Borrow Book\n3. Return Book\n4. Exit")


def get_search_field(option: str) -> Optional[str]:
    """Map menu option to book attribute.

    Args:
        option: User's menu choice.

    Returns:
        Corresponding book attribute or None if invalid.
    """
    return {
        '1': 'title',
        '2': 'author',
        '3': 'genre'
    }.get(option)


def main() -> None:
    """Run the library management system."""
    # Initialize library with sample books
    library = Library([
        Book("The Silent Patient", "Alex Michaelides", "Thriller"),
        Book("Atomic Habits", "James Clear", "Self-help", False),
        Book("Sapiens", "Yuval Noah Harari", "History"),
        Book("Educated", "Tara Westover", "Memoir", False),
        Book("The Midnight Library", "Matt Haig", "Fantasy"),
        Book("Ikigai", "Héctor García", "Philosophy"),
        Book("The Psychology of Money", "Morgan Housel", "Finance", False),
        Book("The Subtle Art of Not Giving a F*ck", "Mark Manson", "Self-help"),
        Book("Becoming", "Michelle Obama", "Biography", False),
        Book("The Lean Startup", "Eric Ries", "Business")
    ])

    print("Welcome to the Library Book Management System")
    
    while True:
        display_menu()
        choice = input("Enter choice: ").strip()

        if choice == '1':
            print("Search by:\n1. Title\n2. Author\n3. Genre")
            opt = input("Enter option: ").strip()
            field = get_search_field(opt)
            if not field:
                print("Invalid option.")
                continue

            keyword = input("Enter keyword: ").strip()
            results = library.search_books(field, keyword)
            if not results:
                print("No matching books found.")
            else:
                for book in results:
                    print(book)

        elif choice == '2':
            title = input("Enter book title to borrow: ").strip()
            try:
                print(library.borrow_book(title))
            except (BookNotFoundException, BookAlreadyBorrowedException) as e:
                print(f"Error: {e}")

        elif choice == '3':
            title = input("Enter book title to return: ").strip()
            try:
                print(library.return_book(title))
            except BookNotFoundException as e:
                print(f"Error: {e}")

        elif choice == '4':
            print("Exiting program. Thank you.")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
