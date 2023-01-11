from controller.CustomerController import CustomerController
from controller.MenuController import MenuController
from controller.OrderController import OrderController
from ui.UIController import menu, invalid


class Controller:
    def __init__(self):
        self.customer_controller = CustomerController()
        self.menu_controller = MenuController()
        self.order_controller = OrderController()

    def main_menu(self):
        opt = menu("Restaurant app", ["Orders", "Menu", "Customers", "<-Exit"])
        if opt is None:
            self.main_menu()

        match opt:
            case 1:
                self.order_controller.menu()
                self.main_menu()
            case 2:
                self.menu_controller.menu()
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
