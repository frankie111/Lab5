def menu(title_, options):
    title(title_)

    print_numbered_list(options)

    inp = input("->")

    if not inp.isnumeric() or int(inp) not in range(1, len(options) + 1):
        invalid()
        return None

    return int(inp)


def invalid():
    print("Invalid option!")


def title(txt):
    print(f"--{txt}--")


def print_numbered_list(lis):
    for i in range(len(lis)):
        print(f"{i + 1}. {lis[i]}")
