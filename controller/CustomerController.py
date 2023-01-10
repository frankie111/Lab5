from models.Customer import Customer
from repository.CustomerRepo import CustomerRepo
from ui.UIController import menu, invalid, title, print_numbered_list


class CustomerController:
    def __init__(self):
        self.customer_repo = CustomerRepo("repository/database/customers.txt")

    def menu(self):
        opt = menu("Customer", ["Add", "Show All", "Update", "Search", "Remove", "<-Exit"])
        if opt is None:
            self.menu()

        match opt:
            case 1:
                self.add()
                self.menu()
            case 2:
                self.show_all()
                self.menu()
            case 3:
                self.update()
                self.menu()
            case 4:
                self.search()
                self.menu()
            case 5:
                self.remove()
                self.menu()
            case 6:
                # return to caller
                pass
            case _:
                invalid()
                self.menu()

    def add(self):
        title("Add customer")
        name = input("Name: ")
        address = input("Address: ")
        customer = Customer(0, name, address)
        self.customer_repo.add(customer)

    def show_all(self):
        title("List of customers")
        customers = self.customer_repo.load()
        print_numbered_list(customers)

    def update(self):
        title("Update customer")
        customers = self.customer_repo.load()
        opt = menu("Which customer to update?", customers)
        if opt is None:
            self.update()

        print("Enter a new value or press enter to keep the current value: ")
        name = input("Name: ")
        address = input("Address: ")

        if name != "":
            customers[opt - 1].name = name
        if address != "":
            customers[opt - 1].address = address

        self.customer_repo.save(customers)

    def search(self, print_list=True):
        title("Search customer")
        name = input("Name: ")
        address = input("Address: ")

        filtered = self.customer_repo.search(name or None, address or None)
        if print_list:
            print_numbered_list(filtered)
        return filtered

    def remove(self):
        customers = self.customer_repo.load()
        title("Remove customer")
        opt = menu("Select by", ["show list", "search"])
        if opt is None:
            self.remove()

        if opt == 1:
            opt1 = menu("Select customer to delete", customers)
            if opt1 is None:
                self.remove()
        else:
            customers = self.search(False)
            opt1 = menu("Select customer to delete", customers)
            if opt1 is None:
                self.remove()

        cus = customers[opt1 - 1]
        self.customer_repo.remove(cus)
