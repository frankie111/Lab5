import functools

from models.Identifiable import Identifiable
from functools import reduce


class Order(Identifiable):
    def __init__(self, id_, customer_id, dish_ids, drinks_ids, bill, time_stamp):
        super().__init__(id_)
        self.customer_id = customer_id
        self.dish_ids = dish_ids
        self.drinks_ids = drinks_ids
        self.bill = bill
        self.time_stamp = time_stamp

    def __eq__(self, other):
        return self.customer_id == other.customer_id \
               and self.dish_ids == other.dish_ids \
               and self.drinks_ids == other.drinks_ids

    def __get_items(self, dishes, drinks):
        dish_list = list(filter(lambda dish: dish.id in self.dish_ids, dishes))
        drink_list = list(filter(lambda drink: drink.id in self.drinks_ids, drinks))
        return dish_list + drink_list

    def generate_costs(self, dishes, drinks):
        items_list = self.__get_items(dishes, drinks)
        costs = functools.reduce(lambda s, item: s + item.price, items_list, 0)
        return costs

    def __generate_bill(self, dishes, drinks):
        items_list = self.__get_items(dishes, drinks)
        bill = self.generate_costs(dishes, drinks)
        bill_lines = map(lambda item: f"'{item.name}' ... '{item.price}'", items_list)
        bill_lines += f"\nYour bill is '{bill}' $ worth!"

        return reduce(lambda s1, s2: s1 + '\n' + s2, bill_lines)

    def show_bill(self, dishes, drinks):
        print(self.__generate_bill(dishes, drinks))
