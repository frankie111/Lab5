from models.Customer import Customer
from repository.CustomerRepo import CustomerRepo

customer1 = Customer(0, "Mihai", "Str. Ciocarliei nr. 19")
customer2 = Customer(1, "Gion", "Str. Luceafarului nr. 27")

repo = CustomerRepo("customers.txt")

repo.save([customer1, customer2])


def search_customer_by_name_test():
    c1 = repo.search("mih")[0]
    c2 = repo.search("ion")[0]

    assert c1 == customer1 and c2 == customer2


def search_customer_by_address():
    c1 = repo.search(address="cioc")[0]
    c2 = repo.search(address="farului")[0]

    assert c1 == customer1 and c2 == customer2


def update_customer_name():
    repo.update(customer1, "Andrei")
    c1 = repo.load()[0]

    assert c1.name == "Andrei"


search_customer_by_name_test()
search_customer_by_address()
update_customer_name()
