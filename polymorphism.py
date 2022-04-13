# POLYMORPHISM OVERLOADING AND OVERRIDING

from xml.dom.minidom import NamedNodeMap


class Employee:
    __minSalary = 12000
    maxSalary = 50000
    companyName = "Working Corps"

    def __init__(self, name, salary, department):
        self.__name = name
        self.__salary = salary
        self._department = department

    def _showData(self):
        print("Employee Name = "+self.__name)
        print("Salary = "+self.__salary)
        print("Department = "+self._department)

    def _getIncome(self):
        return self.__salary * 12

    def __str__(self):
        return ("Employee Name ={}, Salary ={},Department = {}".format(self.__name, self.__salary, self._department))


class Accountant(Employee):
    __departmentName = "Accounting"

    def __init__(self, name, salary, age):
        super().__init__(name, salary, self.__departmentName)
        self.__age = age

    def _showData(self):
        super()._showData()
        print("Age = "+self.__age)

    def __str__(self):
        return (super().__str__()+",Age = {} ".format(self.__age))


class Programmer(Employee):
    __departmentName = "Software Development"

    def __init__(self, name, salary, experience, skill):
        super().__init__(name, salary, self.__departmentName)
        self.__exp = experience
        self.__skill = skill

    def _showData(self):
        super()._showData()
        print("Exp = "+self.__exp)
        print("Skill = "+self.__skill)

    def __str__(self):
        return (super().__str__()+",Exp = {},Skill= {} ".format(self.__exp, self.__skill))


class Sales(Employee):
    __departmentName = "Sales"

    def __init__(self, name, salary, area):
        super().__init__(name, salary, self.__departmentName)
        self.__area = area

    def _showData(self):
        super()._showData()
        print("Area = "+self.__area)

    def __str__(self):
        return (super().__str__()+",Area = {} ".format(self.__area))


alice = Accountant("Alice", "10000", "30")
alice._showData()
bruce = Programmer("Bruce", "10000", "3", "Front-End Developer")
bruce._showData()
charlie = Sales("Charlie", "10000", "Bangkok")
charlie._showData()

print(alice.__str__())
print(bruce.__str__())
print(charlie.__str__())
