# Library 1 -----> 1 NewspaperShelve
# Library 1 -----> 2 BookShelve
# Library has (and aware of) Newspaper Shelve
# pictured with an arrow
class Library:
    def __init__(self):
        self.book_shelve = [
            BookShelve(1, "001"),
            BookShelve(2, "002")
        ]

        self.np_shelves = NewsPaperShelve()


class NewsPaperShelve:
    def __init__(self, title):
        self.title = title


class BookShelve:
    def __init__(self, id, book_type):
        self.id = id
        self.book_type = book_type
        self.capacity = 50

    def __str__(self):
        return "BookShelve(id={},book type={}, capacity={}".format(
            self.id,
            self.book_type,
            self.capacity
        )

    def addBook(self, book):
        pass


class Book:
    def __init__(self, isbn, title, book_type):
        self.isbn = isbn
        self.title = title
        self.book_type = book_type
        self.is_lent = False

    def read(self):
        print("Membaca buku {}".format(self.title))

    ## not a python way, only for education, meaning of setter and getter
    # def set_lent(self, is_lent):
    #     if type(self.is_lent) == bool:
    #         self.is_lent = is_lent
    #     else:
    #         pass


class SingingBook(Book):
    def __init__(self, isbn, title, book_type, song_title):
        super().__init__(isbn, title, book_type)
        self.song_title = song_title

    def play(self):
        print("Play {}".format(self.song_title))
