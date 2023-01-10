from functools import reduce

from models.Customer import Customer
from repository.DataRepo import DataRepo


class CustomerRepo(DataRepo):
    def __init__(self, file):
        super().__init__(file)

    def convert_to_string(self, obj_list):
        str_list = list(map(lambda item: f"{item.id},{item.name},{item.address}", obj_list))
        return reduce(lambda s1, s2: s1 + '\n' + s2, str_list)

    def convert_from_string(self, string):

        if string == "":
            return []

        def line_to_dash(line):
            params = line.split(',')
            id_ = 0 if params[0] == '' else int(params[0])
            return Customer(id_, params[1], params[2])

        lines = string.split('\n')
        return list(map(lambda line: line_to_dash(line), lines))

    def search(self, name=None, address=None):
        customers = self.load()
        result = []
        if name is not None:
            result += list(filter(lambda cus: name.lower() in cus.name.lower(), customers))

        if address is not None:
            result += list(filter(lambda cus: address.lower() in cus.address.lower(), customers))

        return result
