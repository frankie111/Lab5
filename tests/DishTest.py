from models.CookedDish import CookedDish
from repository.CookedDishRepo import CookedDishRepo


def add_dish_test():
    repo = CookedDishRepo("dishes.txt")
    dish = CookedDish(0, "Pizza", 450, 12, 15)
    repo.save([dish])

    read_dish = repo.load()[0]
    assert dish == read_dish


add_dish_test()
