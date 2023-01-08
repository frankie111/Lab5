from functools import reduce

from models.Order import Order
from repository.DataRepo import DataRepo


class OrderRepo(DataRepo):
    def __init__(self, file):
        super().__init__(file)

    def convert_to_string(self, obj_list):
        str_list = map(lambda
                           item: f"{item.id},{item.customer_id},{item.dish_ids},{item.drinks_ids},{item.bill},{item.time_stamp}",
                       obj_list)
        return reduce(lambda s1, s2: s1 + '\n' + s2, str_list)

    def convert_from_string(self, string):
        def line_to_dash(line):
            params: list[str] = line.split(',')
            dish_str = params[2].strip(" []").split(',')
            dishes = map(lambda dish: int(dish), dish_str)

            drink_str = params[3].strip(" []").split(',')
            drinks = map(lambda dish: int(dish), drink_str)
            return Order(int(params[0]), int(params[1]), dishes, drinks, int(params[4]), int(params[5]))

        lines = string.split('\n')
        return map(lambda line: line_to_dash(line), lines)


# repo = OrderRepo("gion")
# lis = [Order(1, 12, [1, 3, 5, 7], [2, 4, 6, 8], 43, 10)]
# string = repo.convert_to_string(lis)
# orders = repo.convert_from_string(string)
# string = repo.convert_to_string(orders)
# print(string)

string = "[1, 3, 6]"
string.replace("[", "")
print(string)
