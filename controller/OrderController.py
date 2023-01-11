from controller.CustomerController import CustomerController
from controller.MenuController import MenuController
from models.Order import Order
from repository.OrderRepo import OrderRepo
from ui.UIController import menu, invalid, title


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
                self.add()
                self.menu()
            case 2:
                self.show_all()
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

        drink_ids = []
        if opt != "":
            drink_ids = list(map(lambda id_: drinks[int(id_) - 1].id, opt.split(',')))

        opt = menu("Choose Dishes (comma separated)", dishes, check=False)
        dish_ids = []
        if opt != "":
            dish_ids = list(map(lambda id_: dishes[int(id_) - 1].id, opt.split(',')))

        # select customer:
        opt = menu("Choose customer by", ["show list", "search", "add"])
        if opt is None:
            self.add()

        def select_cust(customers_):
            opt1 = menu("Select customer", customers_)
            if opt1 is None:
                self.add()
            return customers_[opt1 - 1].id

        customer_id = -1
        match opt:
            case 1:
                customer_id = select_cust(customers)
            case 2:
                filtered = self.customer_controller.search(print_list=False)
                customer_id = select_cust(filtered)
            case 3:
                self.customer_controller.add()
                customer_id = customers[-1].id + 1
            case _:
                self.menu()

        new_order = Order(0, customer_id, dish_ids, drink_ids)
        new_order.set_time_stamp()
        new_order.set_costs(drinks, dishes)
        self.order_repo.add(new_order)

    def show_all(self):
        title("Orders List")
        orders = self.order_repo.load()

        for i in range(len(orders)):
            customer = self.customer_controller.customer_repo.find_by_id(orders[i].customer_id)
            drinks = self.menu_controller.drink_repo.find_by_ids(orders[i].drink_ids)
            dishes = self.menu_controller.dish_repo.find_by_ids(orders[i].dish_ids)
            print(f"{i + 1}. {orders[i].to_string(customer, drinks, dishes)}")

    def remove(self):
        pass
