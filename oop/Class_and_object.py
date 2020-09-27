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


if __name__ == "__main__":
    common_shelve = BookShelve(1, "000")
    print(common_shelve)

    religion_shelve = BookShelve(2, "200")
    print(religion_shelve)

    if common_shelve == religion_shelve:
        print("common shelve== religion shelve")
    else:
        print("they are 2 different objects")

    if type(common_shelve) == type(religion_shelve):
        print("They have the same class type")
    else:
        print("They have different class type")
