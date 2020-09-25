class RubberDuck:
    color = "yellow"

    def squezzed(self):
        print("Kwek Kwek")


class AlligatorDentist:
    bitting_teeth = [1, 5, 10]

    def press_teeth(self, tooth_index_number):
        if tooth_index_number in self.bitting_teeth:
            print("BITEE")


if __name__ == "__main__":
    duck = RubberDuck()
    duck.squezzed()

    alligator = AlligatorDentist()
    alligator.press_teeth(1)
    alligator.press_teeth(2)
    alligator.press_teeth(10)
