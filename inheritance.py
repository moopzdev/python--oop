# INHERITANCE AND SUPER
class Person:
    # class variables
    _minAge = 1
    _species = "Homo sapiens"

    # Constructor Function data are now private
    def __init__(self, _name, _age):
        print("An instance of Class Person is created.")
        # setting data on object initialization
        self.__name = _name
        self.__age = _age

    # setter methods

    def setAge(self, newAge):
        self.__age = newAge

    def setName(self, newName):
        self.__name = newName

    # getter methods
    def getName(self):
        return self.__name

    def _getAgeInDays(self):
        return int(self.__age) * 365

    def __str__(self):
        return ("Name= {}, Age = {}".format(self.__name, self.__age))

    # getting all data

    def getDetails(self):
        print("Person's name = {}".format(self.__name))
        print("Person's age = {}".format(self.__age))


class Programmer(Person):
    _job = "Programmer"

    def __init__(self, _name, _age):
        # makes the parameters/data from parent class available to child class
        super().__init__(_name, _age)
    pass


moopz = Programmer("Moo", "30")
# methods inherited from parent class can be called in child class
print(moopz.getName())
print(moopz._job)
print(moopz._Person__age)

# Converting object to string

print("Age in days = {}".format(moopz._getAgeInDays()))
print(moopz.__str__())
