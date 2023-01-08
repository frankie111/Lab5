from functools import reduce

from models.Customer import Customer
from repository.DataRepo import DataRepo


class CustomerRepo(DataRepo):
    def __init__(self, file):
        super().__init__(file)

    def convert_to_string(self, obj_list):
        str_list = map(lambda item: f"{item.id_},{item.name},{item.address}", obj_list)
        return reduce(lambda s1, s2: s1 + '\n' + s2, str_list)

    def convert_from_string(self, string):
        def line_to_dash(line):
            params = line.split(',')
            return Customer(int(params[0]), params[1], params[2])

        lines = string.split('\n')
        return map(lambda line: line_to_dash(line), lines)
