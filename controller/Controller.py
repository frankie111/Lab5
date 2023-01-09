from controller.CustomerController import CustomerController
from ui.UIController import menu, invalid


class Controller:
    def __init__(self):
        self.customer_controller = CustomerController()

    def main_menu(self):
        opt = menu("Restaurant app", ["Orders", "Menu", "Customers", "<-Exit"])
        if not opt.isnumeric():
            self.main_menu()

        opt = int(opt)

        match opt:
            case 1:
                self.main_menu()
            case 2:
                self.main_menu()
            case 3:
                self.customer_controller.menu()
                self.main_menu()
            case 4:
                # Exit Program
                pass
            case _:
                invalid()
                self.main_menu()
