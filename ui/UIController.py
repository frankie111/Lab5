def menu(title_, options):
    title(title_)

    for i in range(len(options)):
        print(f"{i + 1}. {options[i]}")

    return input("->")


def invalid():
    print("Invalid option!")


def title(txt):
    print(f"--{txt}--")
