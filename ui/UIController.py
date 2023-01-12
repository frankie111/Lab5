def menu(title_, options, ttype=0, check=True, print_options=True):
    title(title_, ttype)

    if print_options:
        print_numbered_list(options)

    inp = input("->")
    if check:
        if not inp.isnumeric() or int(inp) not in range(1, len(options) + 1):
            invalid()
            return None

        return int(inp)

    return inp


def invalid():
    print("Invalid option!")


def title(txt, ttype=0):
    types = {0: '-', 1: '='}
    print(f"{types[ttype] * 2}{txt}{types[ttype] * 2}")


def print_numbered_list(lis):
    for i in range(len(lis)):
        print(f"{i + 1}. {lis[i]}")
