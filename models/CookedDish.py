from models.Dish import Dish


class CookedDish(Dish):
    def __init__(self, id_, name, portion_size, price, prep_time):
        super().__init__(id_, name, portion_size, price)
        self.prep_time = prep_time

    def __eq__(self, other):
        return super().__eq__(other) and self.prep_time == other.prep_time

    def __str__(self):
        return f"Name: {self.name}, Size: {self.portion_size}, Price: {self.price}, Preparation Time: {self.prep_time}"