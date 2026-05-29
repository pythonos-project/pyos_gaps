from random import randint


class Head:
    def __init__(self):
        self.xp = ""

    def _check_x_head(self):
        self.xp = str(randint(0, 10000000))
        print("Use X Head from Gaps with runcode " + self.xp)

    def _print_xp(self):
        print("XP:", self.xp)

    def h_4s(self, obj):
        objected_pta3 = randint(0, 10000000)

        if isinstance(obj, str):
            new_object = obj + str(objected_pta3)

        elif isinstance(obj, (int, float)):
            new_object = obj + objected_pta3

        else:
            raise TypeError("Tipo non supportato")

        return new_object
