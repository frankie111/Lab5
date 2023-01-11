from models.Dish import Dish


class Drink(Dish):
    def __init__(self, id_, name, portion_size, price, alcohol):
        super().__init__(id_, name, portion_size, price)
        self.alcohol = alcohol

    def __eq__(self, other):
        return super().__eq__(other) and self.alcohol == other.alcohol

    def __str__(self):
        return f"Name: {self.name}, Size: {self.portion_size}, Price: {self.price}, Alcohol: {self.alcohol}"