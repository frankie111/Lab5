def lis_to_string(lis):
    string = "["
    for el in lis:
        string += str(el) + ';'
    string = string[:-1]
    return string + ']'
