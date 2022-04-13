# POLYMORPHISM OVERLOADING AND OVERRIDING


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
