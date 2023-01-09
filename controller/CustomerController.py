from models.Customer import Customer
from repository.CustomerRepo import CustomerRepo
from ui.UIController import menu, invalid, title


class CustomerController:
    def __init__(self):
        self.customer_repo = CustomerRepo("repository/database/customers.txt")

    def menu(self):
        opt = menu("Customer", ["Add", "Show All", "Update", "Search", "Erase", "<-Exit"])
        if not opt.isnumeric():
            invalid()
            self.menu()

        opt = int(opt)

        match opt:
            case 1:
                self.add()
                self.menu()
            case 2:
                self.show_all()
                self.menu()
            case 3:
                self.menu()
            case 4:
                self.menu()
            case 5:
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
        for i in range(len(customers)):
            print(f"{i + 1}. {customers[i]}")

    def update(self):
        title("Update customer")
        customers = self.customer_repo.load()
        opt = menu("Which customer to update", customers)
        if not opt.isnumeric():
            invalid()
            self.update()

        opt = int(opt)

    def search(self):
        pass

    def remove(self):
        pass
