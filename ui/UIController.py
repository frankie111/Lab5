def menu(title_, options, ttype=0):
    title(title_, ttype)

    print_numbered_list(options)

    inp = input("->")

    if not inp.isnumeric() or int(inp) not in range(1, len(options) + 1):
        invalid()
        return None

    return int(inp)


def invalid():
    print("Invalid option!")


def title(txt, ttype=0):
    types = {0: '-', 1: '='}
    print(f"{types[ttype] * 2}{txt}{types[ttype] * 2}")


def print_numbered_list(lis):
    for i in range(len(lis)):
        print(f"{i + 1}. {lis[i]}")
