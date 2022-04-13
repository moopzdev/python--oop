from accountant import Accountant
from programmer import Programmer
from sales import Sales


alice = Accountant("Alice", "10000", "30")
alice._showData()


print(alice.__str__())


bruce = Programmer("Bruce", "10000", "3", "Front-End Developer")
bruce._showData()

print(bruce.__str__())

charlie = Sales("Charlie", "10000", "Bangkok")
charlie._showData()

print(charlie.__str__())
