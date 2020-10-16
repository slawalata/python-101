from oop.library import Book


class SingingBook(Book):
    def __init__(self, isbn, title, book_type, song_title):
        super().__init__(isbn, title, book_type)
        self.song_title = song_title

    def play(self):
        print("Play {}".format(self.song_title))


class PopupSingingBook(SingingBook):
    def __init__(self, isbn, title, book_type, song_title, is_pop_up):
        super().__init__(self, isbn, title, book_type, song_title)
        self.is_pop_up = is_pop_up


if __name__ == '__main__':
    bethoven_sym_9 = SingingBook("isbn_bethoven", "Symp 9", "001", "Ode To Joy")

    # have parent public attribute
    print(bethoven_sym_9.isbn)

    # have parent public method
    bethoven_sym_9.read()

    # doesnt have parent private __str__() method
    # or any parent private attribute and method
    print(bethoven_sym_9)

    bethoven_sym_9.play()

    normal_book = Book("isbn normal", "Covid 19", "001")
    # book cant play
    # normal_book.play()

    books = [bethoven_sym_9, normal_book]

    bethoven_sym_9.read()
    bethoven_sym_9.play()
    normal_book.read()

    for book in books:
        # generalization
        # all books have can be read
        book.read()

    normal_book.read()
    normal_book.play()

    bethoven_sym_9.read()
    bethoven_sym_9.play()

    print(isinstance(bethoven_sym_9, SingingBook))
    print(isinstance(bethoven_sym_9, Book))

    print(type(bethoven_sym_9))
    print(type(normal_book))

    winnie_the_pooh = PopupSingingBook("ISBN", "Winnie the pooh", "001", "indonesiaraya", False)

    winnie_the_pooh.song_title
    winnie_the_pooh.isbn
    winnie_the_pooh.play()
    winnie_the_pooh.read()
