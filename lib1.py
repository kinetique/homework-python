class Book:
    def __init__(self, title, author, isbn, year_published):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year_published = year_published

    def get_info(self):
        return f"Title: {self.title},\nAuthor: {self.author},\nISBN: {self.isbn},\nYear published: {self.year_published}"


class FictionBook:
    def __init__(self, title, author, isbn, year_published, genre):
        super().__init__(title, author, isbn, year_published)
        self.genre = genre

    def get_info(self):
        return f"{super().get_info()},\nGenre: {self.genre}"


class NonFictionBook:
    def __init__(self, title, author, isbn, year_published, topic):
        super().__init__(title, author, isbn, year_published)
        self.topic = topic

    def get_info(self):
        return f"{super().get_info()},\nTopic: {self.topic}"


class ReferenceBook:
    def __init__(self, title, author, isbn, year_published, description):
        super().__init__(title, author, isbn, year_published)
        self.description = description

    def get_info(self):
        return f"{super().get_info()},\nDescription: {self.description}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, isbn):
        return [book for book in self.books if book.isbn != isbn]

    def get_books(self):
        return [book.get_info() for book in self.books]

    def get_books_by_category(self, category):
        return [book.get_info() for book in self.books if isinstance(book, category)]

    def get_books_by_author(self, author):
        return [book.get_info() for book in self.books if book.author == author]

    def get_books_by_year(self, year_published):
        return [book.get_info() for book in self.books if book.year_published == year_published]


def main():
    library = Library()

    library.add_book(FictionBook("To Kill a Mockingbird", "Harper Lee", "9780061120084", 1960, "Drama"))
    library.add_book(FictionBook("1984", "George Orwell", "9780451524935", 1949, "Dystopian"))
    library.add_book(NonFictionBook("Educated", "Tara Westover", "9780399590504", 2018, "Memoir"))
    library.add_book(NonFictionBook("The Immortal Life of Henrietta Lacks", "Rebecca Skloot", "9781400052189", 2010, "Biography"))
    library.add_book(ReferenceBook("Gray's Anatomy", "Henry Gray", "9781455582327", 1858, "Medical reference for human anatomy"))

    print("All books in library:")
    print(library.get_info())

    print ("Fiction books in library:")
    print(library.get_books_by_category("Fiction"))

    print ("Non-Fiction books in library:")
    print(library.get_books_by_category("NonFiction"))

    print ("Reference books in library:")
    print(library.get_books_by_category("Reference"))

    print("Books by Harper Lee:")
    print(library.get_books_by_author("Harper Lee"))

    print("Books published in 1949:")
    print(library.get_books_by_year(1949))

    library.remove_book("9780399590504")
    print("All books in library after removal:")
    print(library.get_books())


if __name__ == "__main__":
    main()
