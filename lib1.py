class Book:
    def __init__(self, title, author, isbn, year_published):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year_published = year_published

    def get_info(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Year published: {self.year_published}"


class FictionBook:
    pass


class NonFictionBook:
    pass


class ReferenceBook:
    pass


class Library:
    pass

