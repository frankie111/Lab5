from repository.OrderRepo import OrderRepo
from ui.UIController import menu


class OrderController:
    def __init__(self):
        self.order_repo = OrderRepo("repository/database/orders.txt")

    def menu(self):
        opt = menu()
        pass

    def add(self):
        pass

    def remove(self):
        pass

    def update(self):
        pass
