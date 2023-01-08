from models.Dish import Dish


class Drink(Dish):
    def __init__(self, id_, name, portion_size, price, alcohol):
        super().__init__(id_, name, portion_size, price)
        self.alcohol = alcohol

    def __eq__(self, other):
        return super().__init__(other) and self.alcohol == other.alcohol
