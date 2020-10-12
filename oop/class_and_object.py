from oop.library import BookShelve

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
        print(type(common_shelve))
    else:
        print("They have different class type")

