from controller.CustomerController import CustomerController
from controller.MenuController import MenuController
from repository.CustomerRepo import CustomerRepo
from repository.OrderRepo import OrderRepo
from ui.UIController import menu, invalid, title, print_numbered_list


class OrderController:
    def __init__(self):
        self.order_repo = OrderRepo("repository/database/orders.txt")
        self.customer_controller = CustomerController()
        self.menu_controller = MenuController()

    def menu(self):
        opt = menu("Order", ["Add", "Show All", "Remove", "<-Exit"])
        if opt is None:
            self.menu()

        match opt:
            case 1:
                self.show_all()
                self.menu()
            case 2:
                self.add()
                self.menu()
            case 3:
                self.remove()
                self.menu()
            case 4:
                # caller menu will resume
                return
            case _:
                invalid()
                self.menu()

    def add(self):
        title("Add New Order")
        drinks = self.menu_controller.drink_repo.load()
        dishes = self.menu_controller.dish_repo.load()
        customers = self.customer_controller.customer_repo.load()
        opt = menu("Choose Drinks (comma separated)", drinks, check=False)

        drink_list = []
        if opt != "":
            drink_list = list(map(lambda id_: drinks[id_ - 1], opt.split(',')))

        opt = menu("Choose Dishes (comma separated)", dishes, check=False)
        dish_list = []
        if opt != "":
            dish_list = list(map(lambda id_: dishes[id_ - 1], opt.split(',')))

        # select customer:
        opt = menu("Choose customer by", ["show list", "search", "add"])
        if opt is None:
            self.add()

        match opt:
            case 1:
                opt1 = menu("Select customer", customers)
                if opt1 is None:
                    self.add()
            case 2:
                pass
            case 3:
                pass
            case _:
                self.menu()

    def show_all(self):
        title("Orders List")
        orders = self.order_repo.load()
        dishes = self.menu_controller.dish_repo.load()
        drinks = self.menu_controller.drink_repo.load()
        customers = self.customer_controller.load()

        print_numbered_list(orders)

    def remove(self):
        pass
