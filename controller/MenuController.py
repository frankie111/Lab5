from models.CookedDish import CookedDish
from models.Drink import Drink
from repository.CookedDishRepo import CookedDishRepo
from repository.DrinkRepo import DrinkRepo
from ui.UIController import menu, invalid, title, print_numbered_list


class MenuController:
    def __init__(self):
        self.drink_repo = DrinkRepo("repository/database/drinks.txt")
        self.dish_repo = CookedDishRepo("repository/database/cooked_dishes.txt")

    def menu(self):
        opt = menu("Menu", ["Add", "Show All", "Update", "Remove", "<-Exit"])
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
                self.remove()
                self.menu()
            case 5:
                pass
            case _:
                invalid()
                self.menu()

    def add(self):
        title("Add menu item")
        opt = menu("Choose item type", ["drink", "dish"], ttype=1)
        if opt is None:
            self.add()

        if opt == 1:
            self.__add_drink()
        else:
            self.__add_dish()

    def __add_drink(self):
        title("Add Drink")
        name = input("Name: ")
        portion_size = input("Size: ")
        price = input("Price: ")
        alcohol = input("Alcohol: ")
        drink = Drink(0, name, portion_size, price, alcohol)
        self.drink_repo.add(drink)

    def __add_dish(self):
        title("Add dish")
        name = input("Name: ")
        portion_size = input("Portion size: ")
        price = input("Price: ")
        prep_time = input("Preparation time: ")
        dish = CookedDish(0, name, portion_size, price, prep_time)
        self.dish_repo.add(dish)

    def show_all(self):
        title("Menu:")
        title("List of dishes", 1)
        dishes = self.dish_repo.load()
        print_numbered_list(dishes)
        title("List of drinks", 1)
        drinks = self.drink_repo.load()
        print_numbered_list(drinks)

    def update(self):
        title("Update menu item")
        opt = menu("Choose item type", ["drink", "dish"])
        if opt is None:
            self.update()

        if opt == 1:
            self.__update_drink()
        else:
            self.__update_dish()

    def __update_drink(self):
        title("Update Drink")
        drinks = self.drink_repo.load()
        opt = menu("Which drink to update?", drinks)
        if opt is None:
            self.__update_drink()

        print("Enter a new value or press enter to keep the current value")
        name = input("Name: ")
        portion_size = input("Size: ")
        price = input("Price: ")
        alcohol = input("Alcohol: ")

        drink = drinks[opt - 1]

        if name != "":
            drink.name = name
        if portion_size != "":
            drink.portion_size = portion_size
        if price != "":
            drink.price = price
        if alcohol != "":
            drink.alcohol = alcohol

        self.dish_repo.save(drinks)

    def __update_dish(self):
        title("Update Dish")
        dishes = self.dish_repo.load()
        opt = menu("Which dish to update?", dishes)
        if opt is None:
            self.__update_dish()

        print("Enter a new value or press enter to keep the current value")
        name = input("Name: ")
        portion_size = input("Size: ")
        price = input("Price: ")
        prep_time = input("Preparation Time: ")

        dish = dishes[opt - 1]
        if name != "":
            dish.name = name
        if portion_size != "":
            dish.portion_size = portion_size
        if price != "":
            dish.price = price
        if prep_time != "":
            dish.prep_time = prep_time

        self.dish_repo.save(dishes)

    def remove(self):
        title("Remove menu item")
        opt = menu("Choose item type", ["drink", "dish"])
        if opt is None:
            self.remove()

        if opt == 1:
            self.__remove_drink()
        else:
            self.__remove_dish()

    def __remove_drink(self):
        title("Remove Drink")
        drinks = self.drink_repo.load()
        opt = menu("Choose which Drink to remove", drinks)

        if opt is None:
            self.__remove_drink()

        drink = drinks[opt - 1]
        self.drink_repo.remove(drink)

    def __remove_dish(self):
        title("Remove Dish")
        dishes = self.dish_repo.load()
        opt = menu("Choose which Dish to remove", dishes)

        if opt is None:
            self.__remove_dish()

        dish = dishes[opt - 1]
        self.dish_repo.remove(dish)
