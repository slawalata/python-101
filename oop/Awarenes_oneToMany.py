# Both of side aware of each other.
# Newspaper Shelve has (and aware of) Library
# Library has (and aware of) Newspaper Shelve

class NewsPaperShelve:
    def __init__(self, library):
        self.code = "001"
        self.library = library


class Library:
    newsPaperShelves = []

    def add(self, shelves):
        self.newsPaperShelves.append(shelves)


if __name__ == '__main__':
    library = Library()

    kompasShelves = NewsPaperShelve(library)
    suaraPembaruan = NewsPaperShelve(library)

    library.add(kompasShelves)
    library.add(kompasShelves)
