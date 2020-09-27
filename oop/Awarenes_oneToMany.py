# Library 1 -----> 0..* NewspaperShelve
# Library has (and aware of) Newspaper Shelve
# pictured with an arrow

class NewsPaperShelve:
    def __init__(self, id):
        self.id = id


class Library:
    def __init__(self):
        self.newsPaperShelves = []

    def add(self, shelves):
        self.newsPaperShelves.append(shelves)


if __name__ == '__main__':
    library = Library()

    kompasShelves = NewsPaperShelve("KMP")
    suaraPembaruanShelve = NewsPaperShelve("SP")

    library.add(kompasShelves)
    library.add(kompasShelves)
