from models.CookedDish import CookedDish
from models.Customer import Customer
from models.Order import Order
from repository.CookedDishRepo import CookedDishRepo
from repository.CustomerRepo import CustomerRepo

customer_repo = CustomerRepo("customers.txt")
dish_repo = CookedDishRepo("dishes.txt")

customer = Customer(0, "Mihai", "Str. Ciorilor")
customer_repo.save([customer])

dishes = [CookedDish(0, "Pizza", 450, 12, 15), CookedDish(1, "Ciorba de burta", 350, 24, 45)]
dish_repo.save(dishes)

order = Order(0, customer.id, [dishes[0].id, dishes[1].id])

