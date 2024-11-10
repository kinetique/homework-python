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

    def remove_book(self, book):
        self.books.remove(book)

    def get_info(self):
        return [book.get_info() for book in self.books]

    def get_books_by_category(self, category):
        return [book.get_info() for book in self.books if isinstance(book, category)]

    def get_books_by_author(self, author):
        return [book.get_info() for book in self.books if book.author == author]

    def get_books_by_year(self, year_published):
        return [book.get_info() for book in self.books if book.year_published == year_published]


if __name__ == "__main__":
    pass
