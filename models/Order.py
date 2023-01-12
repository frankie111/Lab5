import functools
from datetime import datetime, timedelta
from functools import reduce

from models.Identifiable import Identifiable


class Order(Identifiable):
    def __init__(self, id_, customer_id, dish_ids=None, drink_ids=None, costs=0, time_stamp=""):
        super().__init__(id_)
        if drink_ids is None:
            drink_ids = []
        if dish_ids is None:
            dish_ids = []
        self.customer_id = customer_id
        self.dish_ids = dish_ids
        self.drink_ids = drink_ids
        self.costs = costs
        self.time_stamp = time_stamp

    def __eq__(self, other):
        return self.customer_id == other.customer_id \
            and self.dish_ids == other.dish_ids \
            and self.drink_ids == other.drink_ids

    def __get_items(self, drinks, dishes):
        drink_list = list(filter(lambda drink: drink.id in self.drink_ids, drinks))
        dish_list = list(filter(lambda dish: dish.id in self.dish_ids, dishes))
        return [*drink_list, *dish_list]

    def generate_costs(self, drinks, dishes):
        items_list = self.__get_items(drinks, dishes)
        costs = functools.reduce(lambda s, item: s + item.price, items_list, 0)
        return costs

    def set_costs(self, drinks, dishes):
        self.costs = self.generate_costs(drinks, dishes)

    def generate_bill(self, drinks, dishes):
        items_list = self.__get_items(drinks, dishes)
        if self.costs == 0:
            self.set_costs(drinks, dishes)

        time = datetime.fromisoformat(self.time_stamp).strftime(" %R ")
        etd = datetime.fromisoformat(self.compute_etd(dishes)).strftime(" %R ")

        bill_lines = list(map(lambda item: f"{item.name} ... {item.price}$", items_list))
        bill_lines.append(f"Your bill is {self.costs}$ worth!")
        bill_lines.append(f"Ordered at: {time} -> estimated delivery time: {etd}\n")

        return reduce(lambda s1, s2: s1 + '\n' + s2, bill_lines)

    def show_bill(self, drinks, dishes):
        print(self.generate_bill(drinks, dishes))

    def set_time_stamp(self):
        self.time_stamp = datetime.now().isoformat()

    def to_string(self, customer, drinks, dishes):
        return f"Order '{self.id}' for '{customer.name}' at Address '{customer.address}':\n" \
            + self.generate_bill(drinks, dishes)

    def compute_etd(self, dishes):
        max_prep_time = max(dishes, key=lambda dish: dish.prep_time).prep_time
        etd = datetime.fromisoformat(self.time_stamp) + timedelta(minutes=max_prep_time)
        return etd.isoformat()
