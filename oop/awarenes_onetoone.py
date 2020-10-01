class NewsPaperShelve:
    # Library 1 -----> 0..1 NewspaperShelve
    # Library has (and aware of) Newspaper Shelve
    # pictured with an arrow
    def __init__(self, title):
        self.title = title


class Library:

    def __init__(self):
        self.shelve = None

    def set_shelves(self, shelve):
        self.shelve = shelve


if __name__ == '__main__':
    library = Library()

    kompasShelves = NewsPaperShelve("kompas")

    library.set_shelves(kompasShelves)
