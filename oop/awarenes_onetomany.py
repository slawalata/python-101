# Library 1 -----> 1 NewspaperShelve ----> 0..20 Newspaper.
# Library has (and aware of) Newspaper Shelve and NP shelves has newspaper.
# pictured with an arrow

class Newspaper:
    def __init__(self, name, date):
        self.name = name
        self.date = date


class NewsPaperShelve:
    def __init__(self, id, capacity):
        self.id = id
        self.capacity = capacity
        self.newspapers = [None] * self.capacity


class Library:
    def __init__(self, newspaper_shelve):
        self.newspaper_shelve = newspaper_shelve


if __name__ == '__main__':
    all_newspaper_shelve = NewsPaperShelve(1, 20)
    my_library = Library(all_newspaper_shelve)
