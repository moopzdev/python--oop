from employee import Employee


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


